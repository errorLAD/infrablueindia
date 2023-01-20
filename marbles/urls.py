from django.urls import path
from . import views

urlpatterns = [
    path('', views.marbles, name='marbles'),
    path('<int:id>', views.marble_detail, name='marble_detail'),
    path('marblesearch', views.marblesearch, name='marblesearch'),
]
