from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    age=models.SmallIntegerField(null=False,blank=False)
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ),blank=False,null=False)
    blood_group=models.CharField(max_length=2,choices=(
        ('O+','O Positive'),
        ('O-','O Negative'),
        ('A+','A Positive'),
        ('A-','A Negative'),
        ('B+','B Positive'),
        ('B-','B Negative'),
        ('AB+','AB Positive'),
        ('AB-','AB Negative'),
    ),blank=False,null=False)
    address_lat=models.DecimalField(max_digits=22,decimal_places=16,blank=False,null=False)
    address_long=models.DecimalField(max_digits=22,decimal_places=16,blank=False,null=False)
    #email=models.EmailField(blank=True,null=True)
    mobile_number=models.DecimalField(blank=False,null=False,max_digits=13,decimal_places=0)
    last_blood_donation=models.DateField(blank=True,null=True)
    currently_eligible_for_donation=models.BooleanField(default=True,blank=False,null=False)

    def __str__(self):
        return self.name


