from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<area>[0-9]+)/$', views.index, name='index')
]