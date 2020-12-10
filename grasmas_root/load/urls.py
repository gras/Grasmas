from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', show, name='show'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('RU_SURE/<int:pk>/', RU_SURE, name='RU_SURE'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('add/', add, name='add'),
    path('show/', show, name='show'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
