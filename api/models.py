from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='city_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='city_modified_by')

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='province_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='province_modified_by')

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='country_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='country_modified_by')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_modified_by')

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.Charfield(max_length=200)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='position_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='position_modified_by')

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience_modified_by')

    def __str__(self):
        return self.position

class Technology(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='techonology_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='techonology_modified_by')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.ManyToManyField(Technology, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_modified_by')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.ManyToManyField(Technology, on_delete=models.CASCADE)
    reated_at = models.DateTimeField(auto_add_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_created_by')
    modified_at = models.DateTimeField(auto_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_modified_by')

    def __str__(self):
        return self.name




