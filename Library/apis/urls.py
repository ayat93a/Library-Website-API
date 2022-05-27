from django.urls import path
from .views import  BookAPIListView , BookAPIDetailView


urlpatterns = [
    path('api/book-list' , BookAPIListView.as_view(), name = 'books_api_list'),
    path('api/<int:pk>' , BookAPIDetailView.as_view(), name = 'book_api_detail')
]