from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.
def main(request):
    all_news = News.objects.all()
    context = {
        'all_news': all_news
    }

    return render(request, 'news/index.html', context=context)


def details(request, news_id):
    news = News.objects.get(id=news_id)

    news_data = {
        'news': news
    }

    return render(request, 'news/details.html', context=news_data)


def category(request, category_id):
    news_list = News.objects.filter(category_id=category_id)

    data = {
        'news_list': news_list
    }

    return render(request, 'news/category.html', context=data)