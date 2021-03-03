from django import forms
from .models import Artist

'''Django documentation on forms can be found here https://docs.djangoproject.com/en/3.1/topics/forms/'''

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'label']