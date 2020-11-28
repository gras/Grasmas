from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate', views.populate),
    path('start', views.start),
    path('board', views.board),
    path('present/<str:position>', views.present)
    # path('', views.index, {'pagename': ''}, name='home'),
    # path('<str:pagename>', views.index, name='index'),
]
