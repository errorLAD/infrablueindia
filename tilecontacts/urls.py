from django.urls import path
from . import views

urlpatterns = [
    path('tileinquiry', views.tileinquiry, name='tileinquiry'),
]