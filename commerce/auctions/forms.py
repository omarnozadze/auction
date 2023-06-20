from django.forms import ModelForm
from django import forms
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = "title","description","image_url","price","owner","category"

        widgets = {
            "title": forms.TextInput(attrs = {'class' :'form-control','placeholder':'title'}),
            "description":forms.TextInput(attrs = {'class' :'form-control','placeholder':'Description'}),
           
            
            

        }