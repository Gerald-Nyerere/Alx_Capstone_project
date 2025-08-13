from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'classroom', 'score', 'remarks', 'term', 'year', ' created_at']



 