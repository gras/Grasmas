from django.urls import path
from . import views

urlpatterns = [
    path('populate', views.populate),
    path('start', views.start),
    path('board', views.board),
    path('present/<str:position>', views.present)
]
