Creating a Book Instance in Django Shell

To create a book instance in Django, follow these steps inside the Django shell:

Command:

from bookshelf.models import Book

book = Book.objects.create(
title="1984",
author="George Orwell",
publication_year=1949
)
print(book)

Expected Output:

1984 by George Orwell (1949)

This confirms that the book instance was successfully created in the database.
