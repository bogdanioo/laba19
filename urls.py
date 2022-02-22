from django.urls import path
from . import views
urlpatterns = [


    path("<int:rik>/<int:mis>/<int:den>/", views.news),
    path("<int:rik>/<int:mis>/", views.news),
    path("<int:rik>/", views.news),
    path("", views.news),
]

