Retrieving a Book Instance in Django Shell

To retrieve a book instance in Django, follow these steps inside the Django shell:

Command:

from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected Output:

1984 George Orwell 1949

This confirms that the book instance was successfully retrieved from the database.
