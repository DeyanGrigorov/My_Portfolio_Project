from django.urls import path

from my_portfolio_project.about_me.views import AboutMe

urlpatterns = [
    path('about_me/', AboutMe.as_view(), name='about me')
]

