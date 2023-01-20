from django.urls import path
from . import views

urlpatterns = [
    path('marbleinquiry', views.marbleinquiry, name='marbleinquiry'),
]