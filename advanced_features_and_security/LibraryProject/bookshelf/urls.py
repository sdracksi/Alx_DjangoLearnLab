from django.urls import path
from .views import book_list, book_create, book_edit, book_delete

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/new/', book_create, name='book_create'),
    path('books/<int:book_id>/edit/', book_edit, name='book_edit'),
    path('books/<int:book_id>/delete/', book_delete, name='book_delete'),
]