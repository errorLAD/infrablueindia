from django.contrib import admin
from .models import Contactmarble

# Register your models here.
class ContactMarbleAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'marble_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'marble_title')
    list_per_page = 25

admin.site.register(Contactmarble, ContactMarbleAdmin)