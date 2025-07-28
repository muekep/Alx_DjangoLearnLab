from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library # Import your models

# --- Function-based View ---
def book_list(request):
    """
    Lists all books stored in the database.
    """
    books = Book.objects.all().order_by('title') # Get all books, ordered by title
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# --- Class-based View ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, listing all books available in that library.
    """
    model = Library # Specifies the model this view will operate on
    template_name = 'relationship_app/library_detail.html' # Path to your template
    context_object_name = 'library' # The name of the variable to use in the template

# Create your views here.
"""  """
