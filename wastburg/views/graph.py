from django.views.generic import DetailView
from django.http import Http404, HttpResponse
import json
from Profile import Profile
from datetime import date
from wastburg.models import *
from licence4.settings import KWH_TO_EUROS

class GraphDataView(DetailView):

  def get_object(self):
    if not self.request.user.is_authenticated():
      raise Http404('No user')
    return Lot.objects.get(owner=self.request.user)

  def add_dataset(self, name, dataset):
    self.data.append({
      'label' : name,
      'data' : [[int(d.strftime('%s')) * 1000, v]  for d,v in dataset],
    })

  def render_to_response(self, context, *args, **kwargs):
    self.data = []

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
    if full:
      self.add_dataset('Goals', goal_daily)

    # Add heat
    heat = p.get_bullshit_heat_spendings(self.object.surface, dates, .3, .3)
    if full:
      self.add_dataset('Heat', heat)

    # Add diff
    diff = map((lambda x,y: [x[0], goal + x[1]-y[1]]), heat, goal_daily)
    if not full:
      self.add_dataset('Diff', diff)

    return HttpResponse(json.dumps(self.data, sort_keys=True, indent=2), 'application/json')
