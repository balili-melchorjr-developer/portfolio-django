from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('experiences', ExperienceViewSets, basename='experiences')
router.register('technologies', TechonologyViewSets, basename='technologies')
router.register('categories', CategoryViewSets, basename='categories')
router.register('projects', ProjectViewSets, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]
