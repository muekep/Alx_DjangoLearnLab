# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy # Used for redirecting to named URLs
from django.contrib.auth.decorators import login_required # Optional: for protecting views
from django.contrib.auth import login
from .models import Book, Library # Your existing imports

# relationship_app/views.py

# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required # Import permission_required

from django.views.generic import DetailView
from .models import Book, Library, UserProfile, Author # Import Author for forms
from .forms import BookForm # Import your new form

# --- Existing Views (from previous steps) ---
def book_list(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Authentication Views ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# --- Role-Based Access Control Helper Functions ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_ADMIN

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_LIBRARIAN

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_MEMBER

# --- Role-Based Views ---
@login_required(login_url=reverse_lazy('relationship_app:login'))
@user_passes_test(is_admin, login_url=reverse_lazy('relationship_app:login'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required(login_url=reverse_lazy('relationship_app:login'))
@user_passes_test(is_librarian, login_url=reverse_lazy('relationship_app:login'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required(login_url=reverse_lazy('relationship_app:login'))
@user_passes_test(is_member, login_url=reverse_lazy('relationship_app:login'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --- New Views with Custom Permissions ---

@permission_required('relationship_app.can_add_book', login_url=reverse_lazy('relationship_app:login'))
@login_required(login_url=reverse_lazy('relationship_app:login')) # Ensure logged in before permission check
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:book_list') # Redirect to book list after creation
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_change_book', login_url=reverse_lazy('relationship_app:login'))
@login_required(login_url=reverse_lazy('relationship_app:login'))
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:book_list') # Redirect to book list after update
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit', 'book': book})

@permission_required('relationship_app.can_delete_book', login_url=reverse_lazy('relationship_app:login'))
@login_required(login_url=reverse_lazy('relationship_app:login'))
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:book_list') # Redirect to book list after deletion
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
