from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import date

class Department(models.Model):
    dept = models.CharField(max_length=255)

    def __str__(self):
        return self.dept 

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses', null=True)  # Changed to nullable
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.course_name

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField(max_length=500,null=True)  # Using EmbedVideoField to store video URLs

    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='videos', null=True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos', null=True)
    
    description = models.TextField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title


