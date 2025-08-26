from rest_framework import serializers
from .models import Classroom
from accounts.models import User


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='teacher'))
    teacher = serializers.SlugRelatedField( slug_field='username', queryset=User.objects.filter(role='teacher'))
    class Meta:
        model = Classroom
        fields = ['name', 'grade', 'teacher', 'year']
