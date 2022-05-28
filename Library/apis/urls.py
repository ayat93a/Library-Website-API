from django.urls import path
from .views import  BookAPIListView , BookAPIDetailView , BookAPILCreateView  , BookAPILUpdateView , BookAPILAll , BookAPILedit


urlpatterns = [
    path('api/book-list' , BookAPIListView.as_view(), name = 'books_api_list'),
    path('api/<int:pk>' , BookAPIDetailView.as_view(), name = 'book_api_detail'),
    path('api/create' , BookAPILCreateView.as_view(), name = 'book_api_create'),
    path('api/<int:pk>/update' , BookAPILUpdateView.as_view(), name = 'book_api_update'),
    path('api/<int:pk>/modify' , BookAPILAll.as_view(), name = 'book_api_All'),
    path('api/<int:pk>/edit' , BookAPILedit.as_view(), name = 'book_api_edit'),
]