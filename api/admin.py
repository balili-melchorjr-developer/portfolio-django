from django.contrib import admin

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
admin.site.register(Technology)
admin.site.register(Category)
admin.site.register(Project)