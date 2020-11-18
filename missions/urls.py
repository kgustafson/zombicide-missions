from django.urls import path
from . import views

urlpatterns = [
    path('', views.missions, name='missions-home'),
]
