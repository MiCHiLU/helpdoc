from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import direct_to_template, redirect_to
from views import render

direct_to_template = permission_required("is_staff")(direct_to_template)
render = permission_required("is_staff")(render)

urlpatterns = patterns('',)

urlpatterns += patterns('',
    (r'^$', direct_to_template, {"template":"helpdoc/index.html"}),
    (r'^(?P<app>\w+)/(?P<doc>[0-9a-z-_\.]+)/$', render),
    (r'^(?P<app>\w+)/', redirect_to, {'url' : "index/"}),
)
