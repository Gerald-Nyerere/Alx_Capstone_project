from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsTeacher

# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':  # GET /subjects/
            return [IsAuthenticated(), (IsAdmin() or IsTeacher())]
        elif self.action == 'create':  # POST /subject/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'retrieve':  # GET /subject/<id>/
            return [IsAuthenticated(), (IsAdmin() or IsTeacher())]
        elif self.action in ['update', 'partial_update']:  # PUT /subject/<id>/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'destroy':  # DELETE /subject/<id>/
            return [IsAuthenticated(), IsAdmin()]
        return super().get_permissions()