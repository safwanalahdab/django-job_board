from django.db import models

# Create your models here.

class Category ( models.Model ) : 
    name = models.CharField( max_length = 100 ) 
    def __str__( self ) :
        return self.name 
    
JOB_TYBE = (
    ('full_time' , 'full_time') , 
    ('part_time' , 'part_time') ,
)

class Job ( models.Model ) :
    title = models.CharField( max_length = 100 ) 
    #location 
    job_tybe = models.CharField( max_length = 10 , choices = JOB_TYBE )
    discription = models.TextField( max_length = 1000 ) 
    published_it = models.DateTimeField( auto_now = True ) 
    vacansy  = models.IntegerField( default = 1 ) 
    salary  = models.IntegerField( default = 0 ) 
    expereince = models.IntegerField( default = 1 ) 
    category = models.ForeignKey( 'Category' , on_delete = models.CASCADE )
    def __str__( self ) :
        return self.title 




