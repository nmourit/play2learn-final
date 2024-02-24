from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView

urlpatterns = [
    # Admin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),

    # User Management

    # Local Apps
    path("userscores/", include("userscores.urls")),
    path('', include("games.urls")),
    path('', include("pages.urls")),
    path('reviews/', include("reviews.urls"))
]
