from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'date_publication', 'est_visible')
    list_display_links = ('id', 'titre')
    list_filter = ('est_visible',)
    search_fields = ('titre',)
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)