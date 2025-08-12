from django.db import models
from django.conf import settings

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    

    def __str__(self):
        return f"{self.name}"

