from django.urls import path

from . import views

app_name='accounts'
urlpatterns = [
    path('password-reset/', views.CustomPasswordResetView.as_view(),
    name='password-reset'),
]
