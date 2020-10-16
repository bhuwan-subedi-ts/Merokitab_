from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here

class Product(models.Model):
    FICTION = 'FC'
    ENGINEERING = 'ER'
    SCIENCE = 'SC'
    MANAGEMENT = 'MG'
    LITERATURE = 'LT'
    ARTS = 'AR'
    SCHOOL = 'SC'
    RELIGION = 'RG'
    ENTRANCE = 'ET'
    GOVERNMENT = 'GR'
    MISC = 'MI'
    LAW = 'LA'
    CATEGORY_CHOICES = [
        (FICTION, 'fiction'),
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (MANAGEMENT, 'Managemetn'),
        (LITERATURE, 'Literature'),
        (ARTS, 'Arts'),
        (SCHOOL, 'School Level'),
        (RELIGION, 'Religion'),
        (LAW, 'Law'),
        (ENTRANCE, 'Entrance Preparation'),
        (GOVERNMENT,'Government Jobs'),
        (MISC, 'Miscelleneous'),
    ]
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media')
    details = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.CharField(max_length=6)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,default=MISC,max_length=100)
    featured = models.BooleanField()

class admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=False,blank=False)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()