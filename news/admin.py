from django.contrib import admin
from .models import Category, News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
