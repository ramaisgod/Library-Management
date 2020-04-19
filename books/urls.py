from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', add_books, name='add_new_books'),
    path('download/', download_page, name='download_page'),
]
