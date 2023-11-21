from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.views.generic import ListView, DetailView


class Article(ListView):
    model = Post
    ordering = '-data_cr_st'
    template_name = 'main.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ArticleId(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context