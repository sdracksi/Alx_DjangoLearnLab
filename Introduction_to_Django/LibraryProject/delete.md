Deleting a Book Instance in Django Shell

To delete a book instance in Django, follow these steps inside the Django shell:

Command:

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion

books = Book.objects.all()
print(books.count()) # Should return 0 if no books are left

Expected Output:

0

This confirms that the book instance was successfully deleted from the database.
