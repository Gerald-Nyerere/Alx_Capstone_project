from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsTeacher, IsStudentReadOnly

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action == 'list':  # GET /students/
            return [IsAuthenticated(), IsAdmin() or IsTeacher()]
        elif self.action == 'create':  # POST /students/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'retrieve':  # GET /students/<id>/
            return [IsAuthenticated(), IsAdmin() or IsTeacher() or IsStudentReadOnly()]
        elif self.action in ['update', 'partial_update']:  # PUT /students/<id>/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'destroy':  # DELETE /students/<id>/
            return [IsAuthenticated(), IsAdmin()]
        return super().get_permissions()
    