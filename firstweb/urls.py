from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin interface
    path('', include('base.urls')),  # Include URL patterns from the 'base' app
    path('api/', include('base.api.urls')),  # Include API URL patterns from the 'base' app
]

# Add URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
