from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('customer', 'created')
    ordering=('customer', 'review')
    search_fields=('customer',)
    fieldsets=(
        ('Reviews',{
            'fields':(
            'customer', 'review',
            )
        }),
    )
