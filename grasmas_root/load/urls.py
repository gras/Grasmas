from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('', maintenance, name='maintenance'),
    path('', status, name='status'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('RU_SURE/<int:pk>/', RU_SURE, name='RU_SURE'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('add/', add, name='add'),
    path('show/', show, name='show'),
    path('status/', status, name='status'),
    path('add_lamp/', add_lamp, name='add_lamp'),
    path('preview/<int:pk>/', preview, name='preview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
