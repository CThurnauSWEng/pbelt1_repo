from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^travels$', views.welcome_traveler)     
]
