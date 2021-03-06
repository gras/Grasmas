from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start),
    path('board/', views.board, name='board'),
    path('final/', views.final, name='final'),
    path('present/<str:position>/', views.present),
    path('steal/<str:position>/', views.steal),
]
