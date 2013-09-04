from django.conf.urls import patterns, include, url
from .views import test_view, CreateConditionView

urlpatterns = patterns('',
	url(r'^$', test_view),
	url(r'^conditions/$', CreateConditionView.as_view(), name="condition"),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': "improve/login.html"}),
	url(r'^logout/$', 'django.contrib.auth.views.logout')
)

