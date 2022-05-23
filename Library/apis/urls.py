from django.urls import path
from books.views import  BookListView ,BookDetailView 


urlpatterns = [
    path('api/book-list' , BookListView.as_view(), name = 'books_api_list'),
    path('api/<int:pk>' , BookDetailView.as_view(), name = 'book_api_detail')
]