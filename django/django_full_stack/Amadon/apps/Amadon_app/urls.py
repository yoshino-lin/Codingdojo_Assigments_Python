from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadmon$', views.index),
    url(r'^amadon/buy$', views.checkout),
]
