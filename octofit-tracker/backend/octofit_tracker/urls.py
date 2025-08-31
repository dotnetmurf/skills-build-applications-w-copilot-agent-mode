"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    BASE_URL = f'https://{CODESPACE_NAME}-8000.app.github.dev/api/'
else:
    BASE_URL = 'http://localhost:8000/api/'

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': BASE_URL + 'users/',
        'teams': BASE_URL + 'teams/',
        'activities': BASE_URL + 'activities/',
        'workouts': BASE_URL + 'workouts/',
        'leaderboard': BASE_URL + 'leaderboard/',
    })

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
