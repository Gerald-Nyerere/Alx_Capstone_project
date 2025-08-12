from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'name', 'admission_number', 'gender', 'year', 'date_of_birth', 'classroom ', ' created_at']




 