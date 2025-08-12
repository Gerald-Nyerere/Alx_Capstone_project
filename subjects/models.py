from django.db import models
from django.conf import settings


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    

    def __str__(self):
        return f"{self.name}"

