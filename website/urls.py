from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)