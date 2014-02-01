from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from wastburg.views import *

urlpatterns = patterns('',
  url(r'^/?$', HomeView.as_view(), name="home"),

  # User management
  url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
  url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page' : '/', }),


)

