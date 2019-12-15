from django.contrib import admin
from .models import Newsletter

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_inscription')
    list_display_links = ('id', 'email')
    list_per_page = 25

admin.site.register(Newsletter, NewsletterAdmin)