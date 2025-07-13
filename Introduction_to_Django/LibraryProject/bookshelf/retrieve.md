Retrieve Operation
Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

Output:

# Expected output: The details of the created book.
# Example:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
