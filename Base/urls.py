# Base/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map the home view to the root URL
]
