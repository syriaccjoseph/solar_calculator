
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.calculator_redirect), 
    url(r'^calculator/', include('calculator.urls')),
    url(r'^admin/', admin.site.urls),
]
