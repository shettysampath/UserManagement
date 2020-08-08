from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.app_status, name='usermg-check'),
    path('', views.app_status, name='usermg-check'),
    path('data', views.ExtractData.as_view(), name='usermg-extract'),
]
