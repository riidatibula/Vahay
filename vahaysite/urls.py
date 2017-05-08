from django.conf.urls import url
from . import views

app_name = 'vahaysite'

urlpatterns = [
   url(r'^$', views.home, name='home'),
]