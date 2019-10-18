from django.conf.urls import url
from . import views

urlpatterns = [
    #判断主页面是登录页面还是直接进入主页
    url(r'^$', views.index),
    #注册模块
    url(r'^register$', views.registration),
    #去到新建旅行的页面
    url(r'^new$', views.new),
    #去到编辑页面
    url(r'^edit/(?P<trip_id>\d+)$', views.edit),
    #去到展示页面
    url(r'^trips/(?P<trip_id>\d+)$', views.trips_info),
    #登录后跳转主页
    url(r'^dashboard$', views.login),
    #创建旅行的模块
    url(r'^create_trip$', views.create_trip),
    #更新旅行的模块
    url(r'^edit_trip/(?P<trip_id>\d+)$$', views.edit_trip),
    #取消参加他人的模块
    url(r'^cancel/(?P<trip_id>\d+)$$', views.cancel_trip),
    #登出模块
    url(r'^logout$', views.logout),
    #删除旅行
    url(r'^remove/(?P<trip_id>\d+)$', views.trip_delete),
    #参加旅行
    url(r'^join/(?P<trip_id>\d+)$', views.join_the_trip),
]
