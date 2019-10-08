from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^(?P<number>\d+)/edit$', views.number_edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),
    url(r'^(?P<number>\d+)$', views.number_return),
]
