from django.db import models
from django.contrib.auth.models import AbstractUser
#import username model
from LMSapp_admin.Usermanager import userManager

# Create your models here.

#********************user*******************************

class User(AbstractUser):
     user_type_choice=[
          ('admin','Admin')
     ]
     first_name=models.CharField(max_length=100)
     last_name=models.CharField(max_length=100)
     username=models.CharField(max_length=100)
     email=models.EmailField(unique=True)
     phone=models.CharField(unique=False,max_length=20)
     # password=models.CharField(max_length=100)
     user_type=models.CharField(max_length=50,choices=user_type_choice,default='admin')
     is_active=models.BooleanField(default=True)
     is_staff=models.BooleanField(default=False)
     is_superuser=models.BooleanField(default=False)

     last_login=models.DateTimeField(blank=True,null=True)
     created_on=models.DateTimeField(auto_now_add=True)
     updated_on=models.DateTimeField(auto_now=True)

     #images
     profile_image=models.ImageField(upload_to='user_profile',null=True)

     #required field for django login
     USERNAME_FIELD='email'
     REQUIRED_FIELDS=['username','phone']
     objects=userManager()

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    published_date=models.DateField()
    def __str__(self):
        return f"{self.title}-{self.Author}"
    

class issued_book(models.Model):
    name=models.CharField(max_length=100)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    borrow_date=models.DateTimeField(null=True,blank=True)
    return_date=models.DateTimeField(null=True,blank=True)
    is_active=models.BooleanField(default=True)





