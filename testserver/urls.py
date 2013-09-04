from django.conf.urls import patterns, include, url
import improve.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testserver.views.home', name='home'),
    # url(r'^testserver/', include('testserver.foo.urls')),
		(r'^accounts/', include('registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^improve/', include('improve.urls')),
		#include(improve.urls)),
		url(r'^', include('todo.urls')),
)
