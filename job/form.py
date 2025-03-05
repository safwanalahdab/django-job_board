from django import forms 
from .models import apply 

class Apply_form (forms.ModelForm) :
    class Meta : 
        model = apply 
        fields =  ['name' , 'email' , 'website' , 'cv' , 'cover' ]  

