from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from wastburg.views import *

urlpatterns = patterns('',
  url(r'^/?$', HomeView.as_view(), name="home"),

  # Graph data
  url(r'^graph/data.json', GraphDataView.as_view(), name="graph-data"),

  # User management
  url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
  url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page' : '/', }),


)

