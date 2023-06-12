from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=25,blank=True, null=True) 
    email = models.EmailField(blank=True, null=True) 
    bio = models.TextField(blank=True, null=True) 
    profile_picture = models.ImageField(upload_to='images/')

    def __str__(self): 
        return self.name 
     

     