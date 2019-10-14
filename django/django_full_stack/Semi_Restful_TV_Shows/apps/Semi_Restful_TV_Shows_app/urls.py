from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<show_id>\d+)/update$', views.show_change),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.original_info),
    url(r'^shows/(?P<show_id>\d+)$', views.show_display),
    url(r'^shows/create', views.show_add),
    url(r'^shows$', views.show),
    url(r'^$', views.show_index),
]
