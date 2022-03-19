from django.urls import path

from my_portfolio_project.contact.views import ContactPage

urlpatterns = [
    path('contact/', ContactPage.as_view(), name='contact page'),
]
