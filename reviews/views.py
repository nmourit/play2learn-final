from django.views.generic import DetailView

from .models import Review

class ReviewDetailView(DetailView):
    model = Review

