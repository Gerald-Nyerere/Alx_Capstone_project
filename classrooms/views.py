from django.shortcuts import render
from rest_framework import viewsets
from .models import Classroom
from .serializers import ClassroomSerializer

# Create your views here.
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    