from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, DeleteView, DetailView, UpdateView
)

from .models import Review
from .forms import ReviewForm

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Review Created'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewDetailView(DetailView):
    model = Review

