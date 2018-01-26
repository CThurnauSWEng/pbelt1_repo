from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^login$', views.user_login),
    url(r'^logout$', views.user_logout),
    url(r'^travels$', views.travels),
    url(r'^add_trip$', views.add_trip),
    url(r'^create_trip$', views.create_trip),
    url(r'^destination/(?P<trip_id>\d+)$', views.show_trip),
    url(r'^create$',views.user_create)     
]
