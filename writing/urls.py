from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from writing import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'writing/login.html'}, name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/writing/'}, name = 'logout'),
    url(r'^$', login_required(login_url='/writing/login/')(views.IndexView.as_view()), 		name='index'),
    url(r'^addpaper/$', views.add_paper, name='add_paper'),
    url(r'^(?P<t>[\w|\W]+)/$', views.paper, name = 'paper'),
)
