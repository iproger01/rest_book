from django.urls import path
from .views import *

urlpatterns = [
    path('autor/', AutorView.as_view()),
    path('book/', BooksView.as_view()),
]