from django.urls import path

from . import views

app_name='contact'
urlpatterns = [
    path('contact-us/', views.ContactFormView.as_view(), name='contact-us'),
    path('facebook/', views.FacebookRedirectView.as_view(), name='facebook'),
]
