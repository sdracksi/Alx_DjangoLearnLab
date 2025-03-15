from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

#Explanation:
#	•	list_display → Displays title, author, and publication_year in the admin list view.
#	•	search_fields → Enables search functionality for title and author.
#	•	list_filter → Allows filtering books by publication_year.

