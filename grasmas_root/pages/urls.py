from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate', views.populate),
    path('showgrid', views.showgrid),
    # path('', views.index, {'pagename': ''}, name='home'),
    # path('<str:pagename>', views.index, name='index'),
]
