from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.registration),
    url(r'^success$', views.login),
    url(r'^logout$', views.logout),
]
