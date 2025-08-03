from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('School.urls')),
    path('', include('Student.urls')),
    path('authentication/', include('home_auth.urls')),
]

# ✅ Correct: only appending static URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
