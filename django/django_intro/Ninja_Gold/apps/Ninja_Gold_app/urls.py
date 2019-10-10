from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process_money$', views.process_money),
    url(r'^destroy_session$', views.destroy_session),
    url(r'^goal_input$', views.goal_setting),
    url(r'^$', views.index),
]
