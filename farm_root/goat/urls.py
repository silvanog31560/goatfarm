from django.urls import path

from . import views

app_name='goats'
urlpatterns = [
    path('herd/', views.HerdListView.as_view(), name='herd-list'),
    path('sale/', views.SaleListView.as_view(), name='sale-list'),
    path('past/', views.PastListView.as_view(), name='past-list'),
    path('retired/', views.RetiredListView.as_view(), name='retired-list'),
    path('buck/add', views.BuckCreateView.as_view(), name='buck-add'),
    path('doe/add', views.DoeCreateView.as_view(), name='doe-add'),
    path('buck/<int:pk>', views.BuckDetailView.as_view(), name='buck-detail'),
    path('doe/<int:pk>', views.DoeDetailView.as_view(), name='doe-detail'),
    path('buck/<int:pk>/image/update', views.BuckImagesUpdateView.as_view(),
        name='buck-image-update'),
    path('doe/<int:pk>/image/update', views.DoeImagesUpdateView.as_view(),
        name='doe-image-update'),
    path('doe/<int:pk>/update', views.DoeUpdateView.as_view(),
        name='doe-update'),
    path('buck,<int:pk>/update', views.BuckUpdateView.as_view(),
        name='buck-update'),
    path('doe/<int:pk>/delete', views.DoeDeleteView.as_view(),
        name='doe-delete'),
    path('buck/<int:pk>/delete', views.BuckDeleteView.as_view(),
        name='buck-delete'),
]
