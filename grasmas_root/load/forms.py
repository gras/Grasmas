from django import forms
from pages.models import *


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['giver', 'title', 'desc']
        labels = {
            'giver': 'The person giving the gift',
            'title': 'Short title for the gift (max 30 characters)',
            'desc': 'Short title for the gift (max 120 characters)',
            'image': 'URL for the gift image',
        }
