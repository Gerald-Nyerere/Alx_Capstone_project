from rest_framework import serializers
from .models import Classroom
from accounts.models import User


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='teacher'))
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='student'),many=True)
    class Meta:
        model = Classroom
        fields = ['name', 'grade', 'year']
