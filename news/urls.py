from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name='main'),
    path('details/<int:news_id>', details, name='details'),
    path('category/<int:category_id>', category, name='category')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)