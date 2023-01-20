from django.contrib import admin
from .models import Marble
from django.utils.html import format_html

# Register your models here.

class MarbleAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.marble_photo.url))

    thumbnail.short_description = 'Marble Image'
    list_display = ('id','thumbnail','marble_title', 'city', 'color', 'model', 'year', 'body_style',  'is_featured')
    list_display_links = ('id', 'thumbnail', 'marble_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'marble_title', 'city', 'model', 'body_style')
    list_filter = ('city', 'model', 'body_style')
admin.site.register(Marble, MarbleAdmin)
# Register your models here.
