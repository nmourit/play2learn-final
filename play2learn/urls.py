from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),

    # User Management
    path("account/", include("users.urls")),
    path("account/", include("allauth.urls")),

    # Local Apps
    path("contact/", include("contact.urls")),
    path("userscores/", include("userscores.urls")),
    path("", include("games.urls")),
    path("", include("pages.urls")),
    path("reviews/", include("reviews.urls")),
]
