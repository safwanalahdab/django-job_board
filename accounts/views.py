from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import Signup 
from .models import*
from .models import Profile 
from .forms import UserForm , ProfileForm 
from django.urls import reverse 


# Create your views here.


def signup ( request ) :
   if request.method == "POST" :
      form = Signup( request.POST , request.FILES ) 
      if form.is_valid() : 
         form.save() 
         username = form.cleaned_data['username']        
         password = form.cleaned_data['password1'] 
         user = authenticate( username = username , password = password )  
         login( request , user ) 
         return redirect ('/accounts/profile') 

   else :
      form = Signup()  
      print(form.errors)

   return render ( request , "registration/signup.html", { 'form' : form } )

def profile ( request ) :
   profile = Profile.objects.get( user = request.user )
   return render( request ,"accounts/profile.html",{ 'profile' : profile })

def profile_edit ( request ) :
   profile = Profile.objects.get( user = request.user )
   
   if request.method == 'POST' :
      userform = UserForm( request.POST , instance = request.user ) 
      profileform = ProfileForm( request.POST , request.FILES , instance = profile )
      if userform.is_valid() and profileform.is_valid() :
         userform.save() 
         x = profileform.save( commit = False )
         x.user = request.user 
         x.save() 
         return redirect( reverse('accounts:profile') )
   else : 
      userform = UserForm( instance = request.user ) 
      profileform = ProfileForm( instance = profile ) 
   
   return render( request , "accounts/profile_edit.html" , { 'userform' : userform , 'profileform' : profileform } ) 