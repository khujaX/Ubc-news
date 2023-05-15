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
    path('profile/', profile, name='profile'),
    path('my_news/', my_news, name='my_news'),
    path('news-update/<int:pk>', news_update, name='news-update')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)