from django.urls import path

from .views import ReviewDetailView

app_name = 'reviews'
urlpatterns = [
    path('review/<slug>/', ReviewDetailView.as_view(), name='detail'),
]