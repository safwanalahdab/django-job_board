from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category ( models.Model ) : 
    name = models.CharField( max_length = 100 ) 
    def __str__( self ) :
        return self.name 
    
JOB_TYBE = (
    ('full_time' , 'full_time') , 
    ('part_time' , 'part_time') ,
)

def upload_image ( instance , filename ) :
    imagename , extension = filename.split(".") 
    return "jobs/%s.%s"%(instance.id ,extension)  

class Job ( models.Model ) :
    owner = models.ForeignKey( User , related_name = 'job_owner' , on_delete = models.CASCADE ) # type: ignore
    title = models.CharField( max_length = 100 ) 
    #location 
    job_tybe = models.CharField( max_length = 10 , choices = JOB_TYBE )
    discription = models.TextField( max_length = 1000 ) 
    published_it = models.DateTimeField( auto_now = True ) 
    vacansy  = models.IntegerField( default = 1 ) 
    salary  = models.IntegerField( default = 0 ) 
    expereince = models.IntegerField( default = 1 ) 
    category = models.ForeignKey( 'Category' , on_delete = models.CASCADE )
    img = models.ImageField( upload_to = upload_image ) 
    slug = models.SlugField( null = True , blank = True ) 
    def save( self , *args , **kwargs ) :
        self.slug = slugify(self.title)
        super( Job , self ).save( *args , **kwargs ) 
    def __str__( self ) :
        return self.title 

class apply ( models.Model ) :
    job = models.ForeignKey( Job , related_name = 'apply_job' , on_delete = models.CASCADE )
    name = models.CharField( max_length= 50 ) 
    email = models.EmailField( max_length = 100 ) 
    website = models.URLField() 
    cv = models.FileField( upload_to = 'apply/') 
    cover = models.TextField( max_length = 500 ) 
    created_At = models.DateTimeField( auto_now = True ) 

    def __str__( self ) :
        return self.name 
 



