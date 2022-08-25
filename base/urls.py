from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('niceweb/', views.niceweb, name="niceweb"),
    path('niceweb2/', views.niceweb2, name="niceweb2"),
    path('energy/', views.energy, name="energy"),
    path('', views.index, name="index"),
]
