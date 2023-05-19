from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name='main'),
    path('details/<int:news_id>', details, name='details'),
    path('category/<int:category_id>', category, name='category'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('add-news/', add_news, name='add_news'),
    path('my_news/', my_news, name='my_news'),
    path('profiles/', profiles, name='profiles'),
    path('profile/<int:profile_id>', profile, name='profile'),
    path('update_info', update_info, name='update_info'),
    path('update_image', update_image, name='update_image'),
    path('news-update/<int:pk>', news_update, name='news-update'),
    path('about_news/<int:news_id>', about_news, name='about_news'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)