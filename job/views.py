from django.shortcuts import render
from .models import *
# Create your views here.

def job_list ( request ) : 
    data = Job.objects.all()
    context = {
        'job' : data , 
    } 
    return render( request , 'job/job_list.html', context )

def job_detail( request , id ) : 
    data = Job.objects.get( id = id ) 
    context = {
        'job' : data ,
    }
    return render( request , 'job/job_detial.html' , context ) 