from django.urls import path
from . import views

urlpatterns = [
    path('', views.tiles, name='tiles'),
    path('<int:id>', views.tile_detail, name='tile_detail'),
    path('tilesearch', views.tilesearch, name='tilesearch'),
]