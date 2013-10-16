from django.conf.urls import patterns, include, url
import improve.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^improve/', include(improve.urls)),
    url(r'^', include('todo.urls')),
)
