from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import redirect_to
from views import app_labels, render

app_labels = permission_required("is_staff")(app_labels)
render = permission_required("is_staff")(render)

urlpatterns = patterns('',)

urlpatterns += patterns('',
    (r'^$', app_labels),
    (r'^(?P<app>\w+)/(?P<doc>[0-9a-z-_\.]+)/$', render),
    (r'^(?P<app>\w+)/', redirect_to, {'url' : "index/"}),
)
