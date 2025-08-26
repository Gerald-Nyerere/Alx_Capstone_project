from django.db import models
from django.conf import settings


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.PositiveBigIntegerField(unique=True)
    

    def __str__(self):
        return f"{self.name}"

