Delete Operation
Command:

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the updated book
book.delete()
print(Book.objects.all()) # Confirm deletion by trying to retrieve all books

Output:

# Expected output: Confirmation of deletion and an empty queryset.
# Example:
# (1, {'bookshelf.Book': 1}) # Output from delete() indicating 1 object deleted
# <QuerySet []> # Output from Book.objects.all() showing no books
