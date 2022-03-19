
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_portfolio_project.common.urls')),
    path('', include('my_portfolio_project.about_me.urls')),
    path('', include('my_portfolio_project.contact.urls')),

]
