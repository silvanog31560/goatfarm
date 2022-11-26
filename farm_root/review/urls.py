from django.urls import path

from . import views

app_name='reviews'
urlpatterns = [
    path('', views.ReviewListview.as_view(), name="review-list"),
    path('create-review', views.ReviewCreate.as_view(), name="create-review"),
]
