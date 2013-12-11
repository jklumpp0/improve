from django.conf.urls import patterns, include, url
import improve.urls
from . import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^improve/', include(improve.urls), name='improve'),
    url(r'^', site.bounce),
)
