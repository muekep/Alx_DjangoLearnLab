# relationship_app/forms.py

from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        # You can add widgets for better UI, e.g.:
        # widgets = {
        #     'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 2100}),
        # }

    # Optional: Customize the author queryset if needed (e.g., only active authors)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all().order_by('name')
