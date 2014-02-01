from django.views.generic import ListView
from wastburg.models import Building, Lot

class HomeView(ListView):
  template_name = 'home.html'
  context_object_name = 'buildings'

  def get_queryset(self):
    return Building.objects.all().order_by('name')
