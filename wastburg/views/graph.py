from django.views.generic import DetailView
from django.http import Http404, HttpResponse
import json
from Profile import Profile
from datetime import date
from wastburg.models import *
from licence4.settings import KWH_TO_EUROS
from datetime import timedelta

class GraphDataView(DetailView):
  prediction_days = 120

  def get_object(self):
    if not self.request.user.is_authenticated():
      raise Http404('No user')
    return Lot.objects.get(owner=self.request.user)

  def add_dataset(self, name, dataset, color=None, dashes=False):
    data = {
      'label' : name,
      'data' : [[int(d.strftime('%s')) * 1000, v]  for d,v in dataset],
    }
    if color:
      data['color'] = color
    self.data['sets'].append(data)

  def render_to_response(self, context, *args, **kwargs):
    self.data = {
      'sets' : [],
      'yscale' : {},
    }

    full = False

    # Date Interval
    start = date(2013, 6, 15)
    end = date.today()

    # Add energy
    edays = EnergyDay.objects.filter(lot=self.object, day__gte=start, day__lte=end).order_by('day')
    dates = [d.day for d in edays] # limiting days
    if full:
      self.add_dataset('Energy', [[d.day, (d.elec or 0.0) * KWH_TO_EUROS] for d in edays])

    # Get all djudays
    days = DjuDay.objects.filter(day__in=dates)
    if full:
      self.add_dataset('DJU', [[d.day, d.diff] for d in days])

    # Build profile
    p = Profile()
    goal = p.get_goal(self.object.surface, dates)
    goal_daily = p.get_daily_goals(self.object.surface, dates)

    # Add goal
    #self.add_dataset('Goals', goal_daily)

    # Add scale
    self.data['yscale'] = {
      'min' : goal-goal*0.01,
      'max' : goal+goal*0.01,
    }

    # Add heat
    tweak = self.object.name == 'B122' and -1 or 1
    heat = p.get_bullshit_heat_spendings(self.object.surface, dates, .3, .3)
    heat_set = [[d,tweak*h*0.5 + goal] for d,h in heat]
    self.add_dataset('Conso', heat_set)

    # Get last heat
    lastheat = heat_set[len(heat_set)-1][1] - 0.0015*goal

    # Add BS diff
    diff = map((lambda x,y: [x[0], goal + x[1]-y[1]]), heat, goal_daily)
    doys = [d.timetuple().tm_yday for d in dates]
    predictions = p.predict_costs(doys, self.object.surface)
    dataset = [[dates[i], goal + predictions[i]] for i,doy in enumerate(doys)]
    #self.add_dataset('Diff', dataset)

    # Add predictions
    end -= timedelta(days=2)
    prediction_dates = [end + timedelta(days=i) for i in range(0, self.prediction_days)]
    doys = [d.timetuple().tm_yday for d in prediction_dates]

    predictions = p.predict_costs(doys, self.object.surface)
    dataset = [[prediction_dates[i], lastheat + predictions[i]] for i,doy in enumerate(doys)]
    self.add_dataset('Predictions', dataset, color='#F00', dashes=True)


    # Add straight line to static goal
    self.add_dataset('But', [[d, goal+0.001*goal] for d in dates + prediction_dates])

    return HttpResponse(json.dumps(self.data, sort_keys=True, indent=2), 'application/json')
