from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from results.models import Result
from classrooms.models import Classroom
from subjects.models import Subject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.user = request.user
            student.save()

            return redirect('student_detail', student.id)
        
    else:
        student_form = StudentForm()

    return render(request, 'students/create_student.html', {"student_form" : student_form})

@login_required
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    result = Result.objects.filter(student=student).first()
    classroom = student.classroom
    subjects = Subject.objects.get(classroom=classroom)
    

    return render(
        request, 
        'students/student_detail.html', 
        {
            "student" : student, 
            "result" : result, 
            "classroom" : classroom, 
            "subject" : subject,
            }
        )
