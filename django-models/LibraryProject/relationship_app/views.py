# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy # Used for redirecting to named URLs
from django.contrib.auth.decorators import login_required # Optional: for protecting views
from django.contrib.auth import login
from .models import Book, Library # Your existing imports

# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test # Import new decorators

from django.views.generic import DetailView
from .models import Book, Library, UserProfile # Import UserProfile

# --- Existing Views ---
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
            # UserProfile is automatically created by signal, but ensure it's saved
            # The signal handles creation, so no explicit UserProfile.objects.create here
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

@login_required(login_url=reverse_lazy('relationship_app:login')) # Ensure user is logged in first
@user_passes_test(is_admin, login_url=reverse_lazy('relationship_app:login')) # Redirect if not admin
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
