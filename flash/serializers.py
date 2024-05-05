from rest_framework import serializers
from .models import Topic, Tag, UseCase, Comparison, ComparisonRow

class ComparisonRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonRow
        fields = ['row1', 'row2']
