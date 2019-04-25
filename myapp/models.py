from __future__ import unicode_literals
from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Customer(models.Model):
    Name= models.CharField(max_length=50)
    Place= models.CharField(max_length=50)
    PhoneNumber= models.CharField(max_length=15)
    CarBrand= models.CharField(max_length=50)
    def __str__(self):
        return self.Name
class Gallery(models.Model):
        Imagename= models.CharField(max_length=50)
        Image= models.ImageField(upload_to='media/Gallery')
        def __str__(self):
            return self.Imagename

class Email(models.Model):
    emailid=models.EmailField()
    def __str__(self):
        return self.emailid
