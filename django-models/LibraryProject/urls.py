from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')), # Include your app's URLs
    # You can also give it a prefix, e.g., path('library/', include('relationship_app.urls')),
    # If you use a prefix, the URLs would be /library/books/, /library/libraries/1/, etc.
]
