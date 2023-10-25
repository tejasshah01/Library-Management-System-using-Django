#import models from django

from django.db import models

#creating custom user model

from django.contrib.auth.models import BaseUserManager

# crate user
class userManager(BaseUserManager):
    def create_user(self,email,username,phone="",password=None,**extra_fields):
        if not username:
            raise ValueError("User name is required")
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Contact No is required")
        
        #for save
        user=self.model(email=self.normalize_email(email),username=username,phone=phone,**extra_fields)
        user.set_password(password)
        user.is_active=True
        user.save()
        return user
    
# create super user
    def create_superuser(self,email,username,phone="",password=None,**extra_fields):
        if not password:
            raise ValueError("Password should not be none")
        user=self.create_user(email,username,phone,password)
        #for saving
        user.is_active=True
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
    

