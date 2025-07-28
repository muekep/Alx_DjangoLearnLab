# relationship_app/urls.py

from django.urls import path
from . import views # Import your views

app_name = 'relationship_app' # Namespace for URLs, good practice

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.book_list, name='book_list'),

    # Class-based view for displaying specific library details
    # <int:pk> captures the primary key (ID) of the library from the URL
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
