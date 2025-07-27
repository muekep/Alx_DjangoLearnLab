import os
import django

# Set up Django environment
# This is crucial for running Django queries outside of manage.py commands
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings') # Replace 'your_project_name'
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.db.utils import IntegrityError

def populate_sample_data():
    """
    Populates some sample data for testing the queries.
    This function should ideally be run once or carefully managed
    to avoid duplicate entries.
    """
    print("--- Populating Sample Data (if not exists) ---")

    try:
        # Create Authors
        author1, created = Author.objects.get_or_create(name="Jane Austen")
        if created: print(f"Created Author: {author1.name}")
        author2, created = Author.objects.get_or_create(name="George Orwell")
        if created: print(f"Created Author: {author2.name}")
        author3, created = Author.objects.get_or_create(name="Harper Lee")
        if created: print(f"Created Author: {author3.name}")

        # Create Books
        book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
        if created: print(f"Created Book: {book1.title}")
        book2, created = Book.objects.get_or_create(title="1984", author=author2)
        if created: print(f"Created Book: {book2.title}")
        book3, created = Book.objects.get_or_create(title="To Kill a Mockingbird", author=author3)
        if created: print(f"Created Book: {book3.title}")
        book4, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
        if created: print(f"Created Book: {book4.title}")
        book5, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)
        if created: print(f"Created Book: {book5.title}")

        # Create Libraries
        lib1, created = Library.objects.get_or_create(name="Central City Library")
        if created: print(f"Created Library: {lib1.name}")
        lib2, created = Library.objects.get_or_create(name="University Library")
        if created: print(f"Created Library: {lib2.name}")

        # Add books to libraries (ManyToMany relationship)
        if created or not lib1.books.exists(): # Only add if new or empty
            lib1.books.add(book1, book2, book3)
            print(f"Added books to {lib1.name}")
        if created or not lib2.books.exists():
            lib2.books.add(book2, book4, book5)
            print(f"Added books to {lib2.name}")

        # Create Librarians (OneToOne relationship)
        # Ensure only one librarian per library
        librarian1, created = Librarian.objects.get_or_create(
            name="Alice Smith",
            library=lib1
        )
        if created: print(f"Created Librarian: {librarian1.name} for {lib1.name}")

        librarian2, created = Librarian.objects.get_or_create(
            name="Bob Johnson",
            library=lib2
        )
        if created: print(f"Created Librarian: {librarian2.name} for {lib2.name}")

    except IntegrityError as e:
        print(f"Data population failed due to IntegrityError (e.g., duplicate unique entry): {e}")
    except Exception as e:
        print(f"An error occurred during data population: {e}")
    print("-" * 40)


def query_all_books_by_specific_author(author_name="Jane Austen"):
    """
    Query all books by a specific author.
    (Author to Book: One-to-Many relationship)
    """
    print(f"\n--- Query: All books by {author_name} ---")
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all() # Using the 'related_name' defined in Book model

        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 40)


def list_all_books_in_a_library(library_name="Central City Library"):
    """
    List all books in a library.
    (Library to Book: Many-to-Many relationship)
    """
    print(f"\n--- Query: All books in '{library_name}' ---")
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all() # Using the field name 'books' on Library model

        if books.exists():
            for book in books:
                print(f"- {book.title} (by {book.author.name})")
        else:
            print(f"No books found in '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 40)


def retrieve_librarian_for_a_library(library_name="University Library"):
    """
    Retrieve the librarian for a specific library.
    (Librarian to Library: One-to-One relationship)
    """
    print(f"\n--- Query: Librarian for '{library_name}' ---")
    try:
        library = Library.objects.get(name=library_name)
        # Using the 'related_name' defined on the Librarian model
        # Or, if you directly query from Librarian: Librarian.objects.get(library=library)
        librarian = library.librarian

        print(f"Librarian for '{library.name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 40)


if __name__ == "__main__":
    # --- IMPORTANT ---
    # Replace 'your_project_name' with the actual name of your Django project's
    # main folder (the one containing settings.py and urls.py)
    # e.g., if your project is named 'myproject', it should be 'myproject.settings'

    # Populate data (optional, remove after initial testing if you manage data elsewhere)
    populate_sample_data()

    # Run the queries
    query_all_books_by_specific_author("Jane Austen")
    query_all_books_by_specific_author("George Orwell")
    query_all_books_by_specific_author("NonExistent Author") # Test case

    list_all_books_in_a_library("Central City Library")
    list_all_books_in_a_library("University Library")
    list_all_books_in_a_library("NonExistent Library") # Test case

    retrieve_librarian_for_a_library("Central City Library")
    retrieve_librarian_for_a_library("University Library")
    # To test a library without a librarian (if possible), you'd need to create one:
    # try:
    #     lib_no_librarian, _ = Library.objects.get_or_create(name="No Librarian Library")
    #     print(f"\n--- Query: Librarian for '{lib_no_librarian.name}' ---")
    #     librarian = lib_no_librarian.librarian # This will raise Librarian.DoesNotExist
    # except Librarian.DoesNotExist:
    #     print(f"No librarian found for '{lib_no_librarian.name}'.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

# Create your views here.
