from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.books),
    url(r'^add$', views.addBook),
    url(r'^createBookReview$', views.createBookReview),
    url(r'^createReview$', views.createReview),
    url(r'^createReview$', views.createReview),
    url(r'^delReview$', views.delReview),
    url(r'^(?P<number>\d+)$', views.bookPage),
]