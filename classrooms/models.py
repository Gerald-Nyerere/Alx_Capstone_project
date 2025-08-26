from django.db import models
from django.conf import settings

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=100)  
    grade = models.CharField(max_length=50, default='Grade 1', unique=True)
    teacher = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'teacher'})
    year = models.IntegerField()
    

    def __str__(self):
        return f"{self.name}"

