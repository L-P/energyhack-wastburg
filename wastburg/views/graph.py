from django.views.generic import DetailView
from django.http import Http404, HttpResponse
import json
#from Profile import Profile
from datetime import date
from wastburg.models import *
from licence4.settings import KWH_TO_EUROS

class GraphDataView(DetailView):

  def get_object(self):
    if not self.request.user.is_authenticated():
      raise Http404('No user')
    return Lot.objects.get(owner=self.request.user)

  def render_to_response(self, context, *args, **kwargs):
    data = []

    # Date Interval
    start = date(2013, 6, 15)
    end = date.today()

    # Mean cost (straight line)
    mean = self.object.calc_mean_cost()

    # Add energy
    edays = EnergyDay.objects.filter(lot=self.object, day__gte=start, day__lte=end).order_by('day')
    dates = [d.day for d in edays] # limiting days
    data_edays = {
      'label' : 'Elec',
      'data' : [[int(d.day.strftime('%s')) * 1000, (d.elec or 0.0) * KWH_TO_EUROS] for d in edays],
    }
    data.append(data_edays)

    # Get all djudays
    days = DjuDay.objects.filter(day__in=dates)
    data_djus = {
      'data' : [[int(d.day.strftime('%s')) * 1000, d.diff] for d in days],
      'label' : 'DJU',
    }
    data.append(data_djus)

    '''
    p = Profile()
    goal = p.get_goal(lot.surface)
    heat = p.get_bullshit_heat_spendings(lot.surface, .3, .3)
    doys = range(365)
    goal_daily = p.get_daily_goals(lot.surface)
    diff = map((lambda x,y: goal + x-y), heat, goal_daily)

    data_diff = {
      'color' : 'blue',
      'data' : [{'x':d, 'y':goal_daily[d]} for d in doys],
      'name' : 'Goal',
    }
    '''
    return HttpResponse(json.dumps(data, sort_keys=True, indent=2), 'application/json')
