from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("userscores/", include("userscores.rls")),
    path('', include("games.urls")),
    path('', include("pages.urls"))
]
