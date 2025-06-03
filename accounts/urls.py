from django.urls import path , include 
from . import views
from .views import *
from .models import * 
app_name = 'accounts'

urlpatterns = [
    path('signup/' , views.signup , name = "signup" ) ,
    path('profile/' , views.profile , name = "profile" ) ,
    path('profile/edit' , views.profile_edit , name = "profile_edit" ) ,
    
]

