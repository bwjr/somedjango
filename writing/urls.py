from django.conf.urls import patterns, url

from writing import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addpaper/$', views.add_paper, name='add_paper'),
    url(r'^(?P<t>[\w|\W]+)/$', views.paper, name = 'paper'),
)
