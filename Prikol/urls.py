from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Prikol import settings
from main.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound
