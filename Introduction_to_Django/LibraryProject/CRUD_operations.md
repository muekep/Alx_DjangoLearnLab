Django Shell CRUD Operations for Book Model
This document details the Create, Retrieve, Update, and Delete (CRUD) operations performed on the Book model within the Django shell, including the Python commands used and their expected outputs.

1. Create Operation
Objective: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

Python Command:

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Expected Output (in Django Shell):

# Example: <Book: 1984 by George Orwell (1949)>

2. Retrieve Operation
Objective: Retrieve and display all attributes of the book you just created.

Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

Expected Output (in Django Shell):

Title: 1984
Author: George Orwell
Publication Year: 1949

3. Update Operation
Objective: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984") # Retrieve the book first using its original title
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title) # Confirm the update

Expected Output (in Django Shell):

Nineteen Eighty-Four

4. Delete Operation
Objective: Delete the book you created and confirm the deletion by trying to retrieve all books again.

Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the updated book
book.delete()
print(Book.objects.all()) # Confirm deletion by trying to retrieve all books

Expected Output (in Django Shell):

(1, {'bookshelf.Book': 1}) # Output from delete() indicating 1 object deleted
<QuerySet []> # Output from Book.objects.all() showing no books
