from rest_framework import serializers
from .models import Result
from students.models import Student
from subjects.models import Subject
from classrooms.models import Classroom


class ResultSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(slug_field='name', queryset=Student.objects.all())
    subject = serializers.SlugRelatedField(slug_field='name', queryset=Subject.objects.all())
    classroom = serializers.SlugRelatedField(slug_field='name', queryset=Classroom.objects.all())
    
    class Meta:
        model = Result
        fields = ['student', 'subject', 'classroom', 'score', 'remarks', 'term', 'year', 'created_at']
