from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .forms import SubjectForm
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsTeacher


# Create your views here.

# List all subjects
@login_required
def subject_list_view(request):
    subjects = Subject.objects.all()
    return render(request, "subjects/subject_list.html", {"subjects": subjects})

# Create a new subject
@login_required
def subject_create_view(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subject_list")
    else:
        form = SubjectForm()
    return render(request, "subjects/subject_form.html", {"form": form})

# View subject detail
@login_required
def subject_detail_view(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, "subjects/subject_detail.html", {"subject": subject})

#DRF for api endpoints
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