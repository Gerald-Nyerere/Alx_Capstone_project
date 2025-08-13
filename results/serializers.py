from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'classroom', 'score', 'remarks', 'term', 'year', 'created_at']
