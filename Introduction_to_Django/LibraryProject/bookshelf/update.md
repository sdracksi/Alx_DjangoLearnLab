Updating a Book Instance in Django Shell

To update a book instance in Django, follow these steps inside the Django shell:

Command:

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

Expected Output:

Nineteen Eighty-Four

This confirms that the book title was successfully updated in the database.
