from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<book_id>\d+)$', views.display_book),
    url(r'^authors/(?P<author_id>\d+)$', views.display_author),
    url(r'^book_author_add/(?P<book_id>\d+)$', views.add_author_to_book),
    url(r'^author_book_add/(?P<author_id>\d+)$', views.add_book_to_author),
    url(r'^authors$', views.authors),
    url(r'^book_add$', views.book_add),
    url(r'^author_add$', views.author_add),
]
