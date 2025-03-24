from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

#  Set up the router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Adds all CRUD endpoints from the ViewSet
]