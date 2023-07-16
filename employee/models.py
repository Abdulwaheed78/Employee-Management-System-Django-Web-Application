import email
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Department(models.Model):
    name=models.CharField(max_length=40)
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    edu=models.CharField(max_length=50)
    prol=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    exsalary=models.IntegerField()
    deptname=models.CharField(max_length=50)
    about=models.CharField(max_length=200) 
    image = models.ImageField(upload_to='images') 
    
class Slider(models.Model):
    img=models.FileField(upload_to='images/slider')


