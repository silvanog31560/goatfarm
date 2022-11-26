from django.contrib import admin
from .models import Buck, Doe, Photo

@admin.register(Buck)
class BuckAdmin(admin.ModelAdmin):
    list_display=('name',)
    ordering=('name',)
    search_fields=('name',)
    fieldsets=(
        ('Buck',{
            'fields':(
            ('name', 'dob'), 'test_result', 'profile_pic',
            'status','availability','comments'
            )
        }),
        ('Parents', {
            'classes': ('collapse',),
            'fields':(
                ('sire', 'dam'), ('ss', 'sd'), ('ds', 'dd')
                )
        }),
    )

@admin.register(Doe)
class DoeAdmin(admin.ModelAdmin):
    list_display=('name',)
    ordering=('name',)
    search_fields=('name',)
    fieldsets=(
        ('Doe',{
            'fields':(
            ('name', 'dob'), 'test_result', 'profile_pic',
            'status','availability','comments'
            )
        }),
        ('Bred',{
            'classes': ('collapse',),
            'fields':(
            'bred_status', 'bred_to', 'due'
            )
        }),
        ('Parents', {
            'classes': ('collapse',),
            'fields':(
                ('sire', 'dam'), ('ss', 'sd'), ('ds', 'dd')
                )
        }),
    )

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('goat', 'image', 'description',)
    ordering=('description',)
    search_fields=('goat',)
