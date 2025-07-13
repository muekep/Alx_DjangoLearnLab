Update Operation
Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984") # Retrieve the book first
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title) # Confirm the update

Output:

# Expected output: The updated title.
# Example: Nineteen Eighty-Four
