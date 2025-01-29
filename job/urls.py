from django.urls import path , include 
from . import views
from .views import *
  
urlpatterns = [
    path('' , views.job_list ) ,
    path('<int:id>' , views.job_detail )
]