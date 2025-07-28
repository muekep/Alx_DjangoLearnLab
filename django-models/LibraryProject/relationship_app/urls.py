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
