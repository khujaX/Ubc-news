from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from django.core.paginator import Paginator
from django.contrib import messages

from .forms import LoginForm, RegisterForm,  NewsAddForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout


# Create your views here.
def main(request):
    searched = request.GET.get('search_word')
    if searched:
        all_news = News.objects.filter(title__contains=searched)
    else:
        all_news = News.objects.all()

    paginator = Paginator(all_news, 6)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    context = {
        'all_news': all_news,
        'page_obj': page_objects
    }

    return render(request, 'news/index.html', context=context)


def details(request, news_id):
    news = News.objects.get(id=news_id)

    news_data = {
        'news': news
    }

    return render(request, 'news/details.html', context=news_data)


@login_required
def category(request, category_id):
    searched = request.GET.get('search_word')
    if searched:
        news_list = News.objects.filter(category_id=category_id, title__contains=searched)
    else:
        news_list = News.objects.filter(category_id=category_id)

    paginator = Paginator(news_list, 5)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    data = {
        'news_list': news_list,
        'page_obj': page_objects
    }

    return render(request, 'news/category.html', context=data)


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'news/login.html', {'form': form})
    
    elif request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username,password=password)
                if user:
                    auth_login(request, user)
                    messages.success(request, f'Hi {username.title()}, welcome back!')
                    return redirect('main')
            
            # form is not valid or user is not authenticated
            messages.error(request,f'Invalid username or password')
            return render(request,'news/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    messages.success(request, f'You have been successfully logged out')
    return redirect('login')


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'news/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, 'news/register.html', {'form': form})


@login_required
def add_news(request):
    if request.method == 'GET':
        form = NewsAddForm()
        return render(request, 'news/news_add.html', {'form': form})

    if request.method == 'POST':
        form = NewsAddForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.publisher = request.user
            news.save()
            messages.success(request, 'News added successfully')
            return redirect('add_news')
        else:
            messages.error(request, 'Something went wrong')
            return render(request, 'news/news_add.html', {'form': form})
