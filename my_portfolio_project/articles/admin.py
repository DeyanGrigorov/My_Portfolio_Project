from django.contrib import admin

# Register your models here.
from my_portfolio_project.articles.models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'author')
