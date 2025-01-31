from django.urls import path , include 
from . import views
from .views import *
app_name = "job" 

urlpatterns = [
    path('' , views.job_list ) ,
    path('<int:id>' , views.job_detail , name = "job_detail" )
]