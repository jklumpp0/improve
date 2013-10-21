from django.conf.urls import patterns, include, url
from .views import test_view, CreateConditionView, create_type_view, edit_user_view, test_manual_view

urlpatterns = patterns('',
	url(r'^$', test_view),
    url(r'^test/$', test_manual_view, name='manual_view'),
	url(r'^conditions/$', CreateConditionView.as_view(), name="condition"),
	url(r'^settings/$', edit_user_view, name='edit_user'),
	url(r'^create_metric/$', create_type_view, name="condition_types"),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': "improve/login.html"}),
	url(r'^logout/$', 'django.contrib.auth.views.logout')
)

