from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from my_portfolio_project.articles.models import Article


def show_articles(request):
    articles = Article.objects.all()
    show_articles_paginator = Paginator(articles, 3)
    page_num = request.GET.get('page')
    page = show_articles_paginator.get_page(page_num)

    context = {
        'page': page,
        'articles': articles
    }
    return render(request, 'works.html', context)


class SearchResultsView(ListView):
    model = Article
    template_name = 'works.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_title'] = self.request.GET.get('q_title')
        context['query_author'] = self.request.GET.get('q_author')
        return context

    def get_queryset(self):
        query_title = self.request.GET.get('q_title')
        query_author = self.request.GET.get('q_author')

        object_list = Article.objects.filter(
            Q(title__icontains=query_title), Q(author__icontains=query_author),
        )

        return object_list
