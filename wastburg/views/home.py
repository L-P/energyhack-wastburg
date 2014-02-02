from django.views.generic import DetailView
from wastburg.models import Building, Lot, DjuDay
from datetime import date
from django.http import HttpResponseRedirect

class HomeView(DetailView):
  context_object_name = 'lot'
  template_name = 'home/private.html'

  def get(self, *args, **kwargs):

    # Minimal page for public
    if not self.request.user.is_authenticated():
      return HttpResponseRedirect('/login')

    return super(HomeView, self).get(*args, **kwargs)

  def get_object(self):
    return Lot.objects.get(owner=self.request.user)

  def get_context_data(self, *args, **kwargs):
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context['days'] = self.object.days.order_by('day')
    context['djus'] = self.load_djus()
    context['season'] = self.object.check_season(date.today())
    return context

  def load_djus(self):
    djus = DjuDay.objects.filter(day__in=[d.day for d in self.object.days.all()])
    out = {}
    for d in djus:
      out[d.day] = d
    return out

