from django.urls import path

from .views import *

urlpatterns = [
    path('', employee, name='home'),
    path('search/', search_results, name='search'),
]