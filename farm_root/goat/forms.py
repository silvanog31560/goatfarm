from django import forms
from django.forms.models import inlineformset_factory

from .models import Photo, Doe, Buck

class DoeForm(forms.ModelForm):

    class Meta():
        model = Doe
        fields = '__all__'
        widgets = {
            'dob':forms.NumberInput(attrs={'type': 'date'}),
            'due':forms.NumberInput(attrs={'type': 'date'}),
        }

class BuckForm(forms.ModelForm):

    class Meta():
        model = Buck
        fields = '__all__'
        widgets = {
            'dob':forms.NumberInput(attrs={'type': 'date'}),
        }

DoeImagesFormset = inlineformset_factory(
    Doe, Photo, fields=('image', 'description',)
    )

BuckImagesFormset = inlineformset_factory(
    Buck, Photo, fields=('image', 'description',)
    )
