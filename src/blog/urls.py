from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from jape_officiel import settings
from .views import base_view, image_view, home_view

urlpatterns = [
    path('', home_view, name="home_view"),
    path('base', base_view, name="base_view"),
    path('1', image_view, name="image_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
