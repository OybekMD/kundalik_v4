from django.shortcuts import render
from rest_framework import generics
from .models import PersonModel, StudentModel, TeacherModel
from .serializers import PersonSerializer, StudentSerializer, TeacherSerializer
from .permissions import IsOwnerPermission

class AllCreateAccountView(generics.ListCreateAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer

# Create your views here.
