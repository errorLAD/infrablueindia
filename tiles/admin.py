from django.contrib import admin
from .models import Tile
from django.utils.html import format_html

# Register your models here.

class TileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.tile_photo.url))

    thumbnail.short_description = 'Tile Image'
    list_display = ('id','thumbnail','tile_title', 'city', 'color', 'model', 'year', 'body_style',  'is_featured')
    list_display_links = ('id', 'thumbnail', 'tile_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'tile_title', 'city', 'model', 'body_style')
    list_filter = ('city', 'model', 'body_style')
admin.site.register(Tile, TileAdmin)
