from django.conf.urls import url
from . import views

app_name = 'vahaysite'

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^logout/$', views.logout_view, name='logout'),
   url(r'^(?P<username>[\w\-]+)/$', views.profile, name='profile'),
   url(r'^(?P<username>[\w\-]+)/add-vahay/$', views.addVahay, name='addVahay'),
]