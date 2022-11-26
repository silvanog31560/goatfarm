from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Review

class ReviewListview(ListView):
    model = Review
    paginate_by = 10

class ReviewCreate(CreateView):
    model = Review
    fields = ('customer','review',)
    success_url = reverse_lazy('reviews:review-list')
