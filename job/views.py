from django.shortcuts import render
from .models import * 
from django.core.paginator import Paginator
from .form import Apply_form
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

def job_detail( request , slug ) : 
    data = Job.objects.get( slug = slug ) 

    if request.method == 'POST' : 
        form = Apply_form( request.POST , request.FILES ) 
        if form.is_valid() : 
            my_form = form.save( commit = False )
            my_form.job = data
            my_form.save()  
    else : 
        form = Apply_form() 

    context = {
        'job' : data ,
        'form' : form ,

    }

    return render( request , 'job/job_detial.html' , context ) 