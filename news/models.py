from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['id']


class News(models.Model):
    publisher = models.ForeignKey(User, related_name='publisher', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    media = models.ImageField(upload_to="news-media/%Y/%m/%d/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} news of {self.category}'

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['-id']
