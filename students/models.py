from django.db import models
from django.conf import settings
from classrooms.models import Classroom

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    admission_number = models.IntegerField(unique=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    classroom =  models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name}"

