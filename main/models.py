
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    address = models.TextField()
    profile_image = models.ImageField(null=True, blank=True,upload_to='images/')
    about = models.TextField(null= True, blank=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    office_name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.office_name} - {self.job_position}"
    
    
class Award(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.year}"
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Cv(models.Model):
    cv = models.FileField(null=True, blank= True, upload_to='doc/')

class Contact(models.Model):
    mail = models.EmailField(max_length=200)
    number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.mail