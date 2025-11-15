from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Classroom
from .forms import ClassroomForm
from .serializers import ClassroomSerializer
from accounts.permissions import IsAdmin, IsTeacher, IsStudentReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@login_required
def classroom_list_view(request):
    classrooms = Classroom.objects.all()
    return render(request, "classrooms/classrooms_list.html", {"classrooms": classrooms})

@login_required
def classroom_detail_view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    return render(request, "classrooms/classroom_detail.html", {"classroom": classroom})

@login_required
def classroom_create_view(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("classroom_list")
    else:
        form = ClassroomForm()
    return render(request, "classrooms/classroom_form.html", {"form": form})

@login_required
def classroom_edit_view(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == "POST":
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect("classroom_list")
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, "classrooms/classroom_form.html", {"form": form})

#DRF apis endpoint
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