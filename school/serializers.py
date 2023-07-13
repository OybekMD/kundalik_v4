from rest_framework import serializers
from .models import SchoolModel
from django.shortcuts import get_object_or_404

    
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'
