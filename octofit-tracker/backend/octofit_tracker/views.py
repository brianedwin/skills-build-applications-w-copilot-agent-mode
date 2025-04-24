from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

CODESPACE_URL = "https://crispy-space-umbrella-67g596vjrg2x4ww-8000.app.github.dev"

@api_view(['GET'])
def api_root(request, format=None):
    host = request.get_host()
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        base_url = f"http://{host}"
    else:
        base_url = CODESPACE_URL
    return Response({
        'users': base_url + reverse('user-list'),
        'teams': base_url + reverse('team-list'),
        'activity': base_url + reverse('activity-list'),
        'leaderboard': base_url + reverse('leaderboard-list'),
        'workouts': base_url + reverse('workout-list'),
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
