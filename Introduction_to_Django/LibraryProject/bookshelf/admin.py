# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Define the custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model
    in the Django administration interface.
    """
    # list_display: Controls which fields are displayed on the change list page of the admin.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Adds filters to the right sidebar of the change list page.
    # Users can click on these filters to quickly narrow down the list of books.
    list_filter = ('publication_year', 'author')

    # search_fields: Enables a search box on the change list page.
    # Django will search these fields when a user types into the search box.
    search_fields = ('title', 'author')

    # list_per_page: Sets the number of items to display per page.
    list_per_page = 25

    # ordering: Defines the default ordering for the list of books.
    # Here, books will be ordered by publication_year in descending order,
    # and then by title alphabetically.
    ordering = ('-publication_year', 'title')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)
# Register your models here.
