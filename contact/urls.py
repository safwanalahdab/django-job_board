from django.urls import path , include 
from . import views
from .views import *
from .models import * 
app_name = "job" 

urlpatterns = [
    path('' , views.send_message , name = "contact" ) ,
]

