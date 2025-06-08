from django.contrib.auth.models import User, Group
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView


class ExperienceViewSets(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-created_at')
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]

    

class TechonologyViewSets(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.AllowAny]

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]



