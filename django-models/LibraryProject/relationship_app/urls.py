# relationship_app/urls.py

from django.urls import path
from .views import list_books # Import your views

# relationship_app/urls.py

from django.urls import path
from . import views # Import your views

# Import Django's built-in authentication views directly for cleaner URL patterns
# from django.contrib.auth import views as auth_views # Alternative if you don't wrap them in CustomLoginView/CustomLogoutView

app_name = 'relationship_app' # Namespace for URLs, good practice
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name= '/logout.html'), name='logout'),
]
urlpatterns = [
    # Existing views
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # New Authentication Views
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # Optional: A protected view to test login_required
    # path('protected/', views.protected_view, name='protected_view'),
]
# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Existing views
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication Views
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # New Role-Based Views
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),
]
# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Existing views
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication Views
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # Role-Based Views
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # New Secured Views for Book Operations
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
