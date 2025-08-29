from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Result
from .serializers import ResultSerializer
from accounts.permissions import IsTeacher, IsAdmin

# Create your views here.
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'subject']

    def get_permissions(self):
        if self.action == 'list':  # GET /results/
            return [IsAuthenticated(), (IsAdmin() or IsTeacher())]
        elif self.action == 'create':  # POST /results/
            return [IsAuthenticated(), (IsAdmin() or IsTeacher())]
        elif self.action == 'retrieve':  # GET /results/<id>/
            return [IsAuthenticated()]  # We'll handle ownership in detail
        elif self.action in ['update', 'partial_update']:  # PUT /results/<id>/
            return [IsAuthenticated(), (IsAdmin() or IsTeacher())]
        elif self.action == 'destroy':  # DELETE /results/<id>/
            return [IsAuthenticated(), IsAdmin()]
        elif self.action in ['student_report', 'classroom_report']:
            return [IsAuthenticated()]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        result = self.get_object()
        if request.user.role == 'student' and result.student != request.user:
            return Response({"detail": "You can only view your own result."}, status=status.HTTP_403_FORBIDDEN)
        return super().retrieve(request, *args, **kwargs)

    # Custom endpoint for student report
    @action(detail=False, methods=['get'], url_path='report/(?P<student_id>[^/.]+)')
    def student_report(self, request, student_id=None):
        if request.user.role == 'student' and request.user.id != int(student_id):
            return Response({"detail": "You can only view your own report."}, status=status.HTTP_403_FORBIDDEN)

        results = Result.objects.filter(student_id=student_id)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

    # Custom endpoint for classroom report
    @action(detail=False, methods=['get'], url_path='report/classroom/(?P<classroom_id>[^/.]+)')
    def classroom_report(self, request, classroom_id=None):
        if request.user.role == 'student':
            return Response({"detail": "Students cannot view classroom reports."}, status=status.HTTP_403_FORBIDDEN)

        results = Result.objects.filter(classroom_id=classroom_id)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)