from django.urls import path

from my_portfolio_project.common import views

urlpatterns = [
    path('', views.landing_page, name='landing page'),
]
