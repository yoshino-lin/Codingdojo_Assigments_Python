from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<book_id>\d+)$', views.book_edit),
    url(r'^book_add$', views.book_add),
    url(r'^register$', views.registration),
    url(r'^success$', views.login),
    url(r'^logout$', views.logout),
    url(r'^update/(?P<book_id>\d+)$', views.book_update),
    url(r'^delete_book/(?P<book_id>\d+)$', views.book_delete),
    url(r'^unfavorite/(?P<book_id>\d+)$', views.unfavorite),
    url(r'^addfavorite/(?P<book_id>\d+)$', views.addfavorite),
    url(r'^book_display/(?P<book_id>\d+)$', views.book_display),
]
