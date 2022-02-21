from django.urls import path
from . import views
urlpatterns = [

    path("", views.index, name="index"),
    path("monday", views.monday, name="monday"),
    path("tuesday", views.tuesday, name="tuesday"),
    path("wednesday", views.wednesday, name="wednesday"),
    path("thursday", views.thursday, name="thursday"),
    path("friday", views.friday, name="friday"),
    path("saturday", views.saturday, name="saturday"),
    path("sunday", views.sunday, name="sunday"),
    path("1", views.monday, name="monday"),
    path("2", views.tuesday, name="tuesday"),
    path("3", views.wednesday, name="wednesday"),
    path("4", views.thursday, name="thursday"),
    path("5", views.friday, name="friday"),
    path("6", views.saturday, name="saturday"),
    path("7", views.sunday, name="sunday"),
]