from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def job_list ( request ) : 
    data = Job.objects.all() 

    paginator = Paginator(data, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'job' : page_obj , 
    } 
    return render( request , 'job/job_list.html', context )

def job_detail( request , id ) : 
    data = Job.objects.get( id = id ) 
    context = {
        'job' : data ,
    }

    return render( request , 'job/job_detial.html' , context ) 