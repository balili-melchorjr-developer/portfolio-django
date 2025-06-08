from django.contrib import admin
from django import forms

from django.db import models
from ckeditor.widgets import CKEditorWidget



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




admin.site.register(City)
admin.site.register(Province)
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Experience)


class ExperienceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Experience
        fields = '__all__'

class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm

admin.site.register(Technology)
admin.site.register(Category)
admin.site.register(Project)