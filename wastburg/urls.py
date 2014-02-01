from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from wastburg.views import *

urlpatterns = patterns('',
  url(r'^/?$', HomeView.as_view(), name="home"),
  url(r'^lot/(?P<building>\w+)/(?P<lot>\w+)/?$', LotView.as_view(), name="lot"),
)

