from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin
from django.core.paginator import Paginator

def test(request):
    objects = ['gg', 'wp', 'bb', 'gg1', 'wp2', 'bb3', 'gg4', 'wp5']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})

class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_pro = 'nello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context['title'] = 'Главная страница'
        extra_context['mixin_prop'] = self.get_pro()
        return extra_context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return extra_context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DeleteView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    raise_exception = True

