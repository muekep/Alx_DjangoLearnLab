# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # For signals
from django.dispatch import receiver # For signals

# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Existing models (Author, Library, Librarian, UserProfile) remain the same
# ... (your existing Author, Library, Librarian, UserProfile models here) ...

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta: # --- ADD THIS META CLASS ---
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change existing book"),
            ("can_delete_book", "Can delete a book"),
        ]
        # Optional: You might also want to order books by title by default
        # ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(
        Book,
        related_name='libraries'
    )

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} ({self.library.name} Librarian)"

class UserProfile(models.Model):
    ROLE_ADMIN = 'Admin'
    ROLE_LIBRARIAN = 'Librarian'
    ROLE_MEMBER = 'Member'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_LIBRARIAN, 'Librarian'),
        (ROLE_MEMBER, 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
