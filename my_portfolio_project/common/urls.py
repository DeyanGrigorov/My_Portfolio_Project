from django.urls import path

from my_portfolio_project.common.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='landing page'),
]
