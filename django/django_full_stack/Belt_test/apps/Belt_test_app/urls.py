from django.conf.urls import url
from . import views

urlpatterns = [
    #判断主页面是登录页面还是直接进入主页
    url(r'^$', views.index),
    #注册模块
    url(r'^register$', views.registration),
    #登录后跳转主页
    url(r'^success$', views.login),
    #登出模块
    url(r'^logout$', views.logout),
]
