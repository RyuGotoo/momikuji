from django.urls import path
from . import views

urlpatterns = [
    path('', views.momikuji, name='momikuji')
]
