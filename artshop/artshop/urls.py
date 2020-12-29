from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('Page.urls')),
    path('admin/', admin.site.urls),
]
