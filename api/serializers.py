from django.contrib.auth.models import User, Group
from .models import (
    City,
    Province,
    Country,
    Company,
    Position,
    Experience,
    Technology,
    Category,
    Project
)
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    depth = 1

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):

    position = PositionSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'

    depth = 1

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    technology = TechnologySerializer(read_only=True, many=True)
    
    class Meta:
        model = Category
        fields = '__all__'

    depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    depth = 1