from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("loyalty_app.urls")),
    path("auth/", include("authentication.urls")),
]
