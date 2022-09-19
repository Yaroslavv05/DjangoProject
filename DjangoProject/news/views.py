from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей', 'categoris': categories,})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categoris': categories, 'category': category})

