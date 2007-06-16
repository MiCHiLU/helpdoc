from django.conf.urls.defaults import *
from views import app_labels, render


urlpatterns = patterns('',)

urlpatterns += patterns('',
    (r'^$', app_labels),
    #(r'^(?<app>\w+)/(?P<doc>[0-9a-z-_\.]+)/$', render),
)
