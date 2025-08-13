from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'name', 'admission_number', 'gender', 'date_of_birth', 'classroom', 'created_at']
