
from django.contrib import admin
from django.urls import path, include  # Importa `include` para enlazar otras URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Enlaza las URLs de tu aplicación
]

