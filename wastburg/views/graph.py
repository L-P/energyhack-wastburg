from django.views.generic import DetailView
from django.http import Http404, HttpResponse
from wastburg.models import Lot
import json

#TRASHME
from datetime import date
from random import randint

class GraphDataView(DetailView):

  def get_object(self):
    if not self.request.user.is_authenticated():
      raise Http404('No user')
    return Lot.objects.get(owner=self.request.user)

  def render_to_response(self, context, *args, **kwargs):
    data = [
    {
    "color": "blue",
    "name": "New York",
    "data": [ { "x": 0, "y": 40 }, { "x": 1, "y": 49 }, { "x": 2, "y": 38 }, { "x": 3, "y": 30 }, { "x": 4, "y": 32 } ]
    }, {
    "name": "London",
    "data": [ { "x": 0, "y": 19 }, { "x": 1, "y": 22 }, { "x": 2, "y": 29 }, { "x": 3, "y": 20 }, { "x": 4, "y": 14 } ]
    }, {
    "name": "Tokyo",
    "data": [ { "x": 0, "y": 8 }, { "x": 1, "y": 12 }, { "x": 2, "y": 15 }, { "x": 3, "y": 11 }, { "x": 4, "y": 10 } ]
    }
    ]

    return HttpResponse(json.dumps(data, sort_keys=True, indent=2), 'application/json')
