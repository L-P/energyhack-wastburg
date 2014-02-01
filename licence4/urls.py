from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

from django.contrib import admin
admin.autodiscover()
print settings.STATIC_ROOT
urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'', include('wastburg.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
