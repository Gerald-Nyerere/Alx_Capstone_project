from rest_framework import serializers
from django.db.models import Sum
from .models import Result
from students.models import Student
from subjects.models import Subject
from classrooms.models import Classroom


class ResultSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(slug_field='name', queryset=Student.objects.all())
    subject = serializers.SlugRelatedField(slug_field='name', queryset=Subject.objects.all())
    classroom = serializers.SlugRelatedField(slug_field='name', queryset=Classroom.objects.all())
    total_marks = serializers.SerializerMethodField()
    
    class Meta:
        model = Result
        fields = ['student', 'subject', 'classroom', 'score', 'total_marks', 'remarks', 'term', 'year', 'created_at']

  
    def get_total_marks(self, obj):
        total = Result.objects.filter(student=obj.student).aggregate(total=Sum('score'))['total']
        return total or 0
