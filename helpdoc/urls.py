from django.conf.urls.defaults import *
from django.contrib.admin.views.decorators import staff_member_required
from views import app_labels, render

app_labels = staff_member_required(app_labels)


urlpatterns = patterns('',)

urlpatterns += patterns('',
    (r'^$', app_labels),
    #(r'^(?<app>\w+)/(?P<doc>[0-9a-z-_\.]+)/$', render),
)
