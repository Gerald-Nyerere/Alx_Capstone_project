from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'admission_number', 'gender', 'date_of_birth', 'classroom']
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-5 py-3 border rounded-2xl focus:ring-2 focus:ring-blue-400 transition shadow-sm",
                "placeholder": "Full Name"
            }),
            "admission_number": forms.TextInput(attrs={
                "class": "w-full px-5 py-3 border rounded-2xl focus:ring-2 focus:ring-blue-400 transition shadow-sm",
                "placeholder": "Admission Number"
            }),
            "gender": forms.Select(attrs={
                "class": "w-full px-5 py-3 border rounded-2xl focus:ring-2 focus:ring-blue-400 transition shadow-sm",
            }),
            "date_of_birth": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full px-5 py-3 border rounded-2xl focus:ring-2 focus:ring-blue-400 transition shadow-sm",
            }),
            "classroom": forms.Select(attrs={
                "class": "w-full px-5 py-3 border rounded-2xl focus:ring-2 focus:ring-blue-400 transition shadow-sm",
            }),
        }




 