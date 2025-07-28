# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy # Used for redirecting to named URLs
from django.contrib.auth.decorators import login_required # Optional: for protecting views

from .models import Book, Library # Your existing imports

# --- Existing Views (from previous step) ---
def book_list(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

from django.views.generic import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- New Authentication Views ---

# Custom Registration View (Function-based)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View (Class-based, using Django's built-in)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    # success_url is handled by LOGIN_REDIRECT_URL in settings.py

# Logout View (Class-based, using Django's built-in)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    # next_page is handled by LOGOUT_REDIRECT_URL in settings.py

# Optional: Example of a protected view
@login_required
def protected_view(request):
    return render(request, 'relationship_app/protected.html') # You'd need to create this template
