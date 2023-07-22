from django.db import models



class Student(models.Model):
    gender_select = (('Null','Select gender'),('Male','Male'),('Female','Female'),('Other','Other'))
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=gender_select,default='Null')
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    avatar = models.FileField(upload_to='Avatar',null=True)
    hobby = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True) 
    class Meta:
        verbose_name_plural = 'Student'
    def __str__(self):
        return self.fname
    
class Course(models.Model):
  
    image = models.FileField(upload_to='Course')
    title = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    fee = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = 'Course'
    def __str__(self):
        return self.title


class Picked(models.Model):
    user_id = models.CharField(max_length=100) 
    Course_id = models.CharField(max_length=100)
    email = models.EmailField() 

    class Meta:
        verbose_name_plural = 'Picked'
    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    class Meta:
        verbose_name_plural = 'Contact'
    def __str__(self):
        return self.email
    
# Create your models here.
