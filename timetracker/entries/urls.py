from django.conf.urls import include, url

from entries import views



urlpatterns = [
    url(r'^entries/$', views.entries, name='entries'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^summary/$', views.summary, name='summary'),
]
