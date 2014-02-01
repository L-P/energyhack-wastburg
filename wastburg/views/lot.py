from django.views.generic import DetailView
from wastburg.models import Lot

class LotView(DetailView):
  template_name = 'lot.html'

  def get_object(self):
    return Lot.objects.get(building__name=self.kwargs['building'], name=self.kwargs['lot'])

  def get_context_data(self, *args, **kwargs):
    context = super(LotView, self).get_context_data(*args, **kwargs)
    context['days'] = self.object.days.order_by('day')
    return context
