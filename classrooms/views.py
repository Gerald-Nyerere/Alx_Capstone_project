from django.shortcuts import render
from rest_framework import viewsets
from .models import Classroom
from .serializers import ClassroomSerializer
from accounts.permissions import IsAdmin, IsTeacher, IsStudentReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer 
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action == 'list':  # GET /classrooms/
            return [IsAuthenticated(), IsAdmin() or IsTeacher()]
        elif self.action == 'create':  # POST /classrooms/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'retrieve':  # GET /classrooms/<id>/
            return [IsAuthenticated(), IsAdmin() or IsTeacher()]
        elif self.action in ['update', 'partial_update']:  # PUT /classroom/<id>/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'destroy':  # DELETE /classrooms/<id>/
            return [IsAuthenticated(), IsAdmin()]
        return super().get_permissions()