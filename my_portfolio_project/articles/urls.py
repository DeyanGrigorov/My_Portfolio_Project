from django.urls import path

from my_portfolio_project.articles.views import show_articles

urlpatterns = (
    path('articles', show_articles, name='articles page'),

)

