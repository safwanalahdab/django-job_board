from django.shortcuts import redirect, render
from django.urls import reverse 
from .models import * 
from django.core.paginator import Paginator
from .form import Apply_form , Add_job
from django.contrib.auth.decorators import login_required
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

@login_required 
def add_job( request ) :    
    if request.method == 'POST' :
        form = Add_job( request.POST , request.FILES )
        if form.is_valid() : 
           myform = form.save( commit = False )
           myform.owner = request.user
           myform.save()
           return redirect(reverse('job:job_list')) 


    else : 
        form = Add_job() 
    return render( request , 'job/add_job.html' , { 'form' : form } )

