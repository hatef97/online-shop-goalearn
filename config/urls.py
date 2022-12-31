from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings
from config.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    # Rosetta i18n
    path('rosetta/', include('rosetta.urls')),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
