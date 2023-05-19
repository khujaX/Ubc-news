from django.contrib import admin
from .models import Category, News, User


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    ordering = ['id']


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id', 'first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')



admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(User, UserAdmin)