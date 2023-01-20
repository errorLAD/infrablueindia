from django.contrib import admin
from .models import Contacttile

# Register your models here.
class ContactTileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'tile_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'tile_title')
    list_per_page = 25

admin.site.register(Contacttile, ContactTileAdmin)