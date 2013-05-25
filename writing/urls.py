from django.conf.urls import patterns, url

from writing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<t>[\w|\W]+)/$', views.paper, name = 'paper'),
)
