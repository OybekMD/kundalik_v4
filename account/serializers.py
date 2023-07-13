from rest_framework import serializers
from .models import PersonModel, StudentModel, TeacherModel
from django.shortcuts import get_object_or_404

    
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

