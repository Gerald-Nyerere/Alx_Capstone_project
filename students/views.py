from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Student
from subjects.models import Subject
from classrooms.models import Classroom
from results.models import Result
from .forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsTeacher, IsStudentReadOnly
from django.db.models import Count

# Create your views here.

# List all students (dashboard)
@login_required
def dashboard_view(request):
    # Counts for cards
    students_count = Student.objects.count()
    classrooms_count = Classroom.objects.count()
    subjects_count = Subject.objects.count()
    results_count = Result.objects.count()

    # Total results per student
    student_totals = (
        Result.objects.values('student__id', 'student__name')
        .annotate(total_results=Count('id'))
        .order_by('-total_results')  # highest first
    )

    context = {
        "students_count": students_count,
        "classrooms_count": classrooms_count,
        "subjects_count": subjects_count,
        "results_count": results_count,
        "student_totals": student_totals,
    }
    return render(request, "dashboard.html", context)

# View student detail
@login_required
def student_detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})

# Create a new student
@login_required
def student_create_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form})

#list student
@login_required
def student_list_view(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

#DRF API ENDPOINT
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
    