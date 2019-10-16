from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.registration),
    url(r'^success$', views.login),
    url(r'^logout$', views.logout),
    url(r'^wall$', views.message_post),
    url(r'^comment_post/(?P<message_id>\d+)$', views.comment_post),
    url(r'^delete/(?P<message_id>\d+)$', views.delete_message),
]
