from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15)
    profession = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='media')
    rating = models.CharField(max_length=50)
    pradesh = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    palika = models.CharField(max_length=50)
    ward_no = models.IntegerField()
    local_add = models.CharField(max_length=50)

class Category(models.Model):
    FICTION = 'Fiction'
    ENGINEERING = 'Engineering'
    SCIENCE = 'Science'
    MANAGEMENT = 'Management'
    LITERATURE = 'Literature'
    ARTS = 'Arts'
    SCHOOL = 'School'
    RELIGION = 'Religion'
    ENTRANCE = 'Entrance'
    GOVERNMENT = 'Government'
    MISC = 'Miscellenous'
    LAW = 'Law'
    
    CATEGORY_CHOICES = [
        (FICTION, 'Fiction'),
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (MANAGEMENT, 'Management'),
        (LITERATURE, 'Literature'),
        (ARTS, 'Arts'),
        (SCHOOL, 'School Level'),
        (RELIGION, 'Religion'),
        (LAW, 'Law'),
        (ENTRANCE, 'Entrance Preparation'),
        (GOVERNMENT,'Government Jobs'),
        (MISC, 'Miscelleneous'),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100,default=MISC)

    def __str__(self):
        return (self.category)

class Product(models.Model):
    FICTION = 'Fiction'
    ENGINEERING = 'Engineering'
    SCIENCE = 'Science'
    MANAGEMENT = 'Management'
    LITERATURE = 'Literature'
    ARTS = 'Arts'
    SCHOOL = 'School'
    RELIGION = 'Religion'
    ENTRANCE = 'Entrance'
    GOVERNMENT = 'Government'
    MISC = 'Miscellenous'
    LAW = 'Law'
    
    CATEGORY_CHOICES = [
        (FICTION, 'Fiction'),
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (MANAGEMENT, 'Management'),
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
    publication = models.CharField(max_length=100, default='xyz')
    ISBN = models.CharField(max_length=100,default='123')
    author = models.CharField(max_length=100,default='writer')
    category = models.CharField(choices=CATEGORY_CHOICES,default=MISC,max_length=100)
    featured = models.BooleanField(null=True)
    abstract = models.TextField(default='This is the abstract')
    status = models.BooleanField(default='True')

    def __str__(self):
        return (self.name)

class admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=False,blank=False)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE)
    comment = models.TextField()
    ratings = models.IntegerField(default=0,
        validators= [MaxValueValidator(5), MinValueValidator(1)], 
    )
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user)