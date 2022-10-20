from django.urls import path

from my_portfolio_project.articles.views import show_articles, details

urlpatterns = (
    path('articles', show_articles, name='articles page'),
    path('details/<int:pk>', details, name='details page'),


)

