from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.core.urls')),
    path('signals/', include('Apps.signals.urls')),
    path('middleware/', include('Apps.middleware.urls')),
]
