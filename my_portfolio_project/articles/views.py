from django.shortcuts import render
from my_portfolio_project.articles.models import Article


def show_articles(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'articles.html', context)
