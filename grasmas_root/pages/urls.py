from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate', views.populate),
    path('start', views.start),
    path('show_gift', views.show_gift)
    # path('', views.index, {'pagename': ''}, name='home'),
    # path('<str:pagename>', views.index, name='index'),
]
