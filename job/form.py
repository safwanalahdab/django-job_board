from django import forms 
from .models import apply , Job

class Apply_form (forms.ModelForm) :
    class Meta : 
        model = apply 
        fields =  ['name' , 'email' , 'website' , 'cv' , 'cover' ]  

class Add_job ( forms.ModelForm ) : 
    class Meta : 
        model = Job 
        fields = '__all__'
        exclude = ('owner','slug',)  