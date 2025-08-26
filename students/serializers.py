from rest_framework import serializers
from .models import Student
from classrooms.models import Classroom

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.SlugRelatedField(slug_field='grade', queryset=Classroom.objects.all())
    class Meta:
        model = Student
        fields = ['name', 'admission_number', 'gender', 'date_of_birth', 'classroom', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
