from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta, datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User.objects.create(email='thundergod@mhigh.edu', name='Thunder God', password='thundergodpassword'),
            User.objects.create(email='metalgeek@mhigh.edu', name='Metal Geek', password='metalgeekpassword'),
            User.objects.create(email='zerocool@mhigh.edu', name='Zero Cool', password='zerocoolpassword'),
            User.objects.create(email='crashoverride@mhigh.edu', name='Crash Override', password='crashoverridepassword'),
            User.objects.create(email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]

        # Create teams
        blue_team = Team.objects.create(name='Blue Team')
        gold_team = Team.objects.create(name='Gold Team')
        
        # Add members to teams
        blue_team.members.add(users[0], users[1], users[2])
        gold_team.members.add(users[3], users[4])

        # Create activities
        activities = [
            Activity.objects.create(
                user=users[0],
                type='Cycling',
                duration=60,
                date=timezone.now()
            ),
            Activity.objects.create(
                user=users[1],
                type='Crossfit',
                duration=120,
                date=timezone.now()
            ),
            Activity.objects.create(
                user=users[2],
                type='Running',
                duration=90,
                date=timezone.now()
            ),
            Activity.objects.create(
                user=users[3],
                type='Strength',
                duration=30,
                date=timezone.now()
            ),
            Activity.objects.create(
                user=users[4],
                type='Swimming',
                duration=75,
                date=timezone.now()
            ),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard.objects.create(user=users[0], score=100),
            Leaderboard.objects.create(user=users[1], score=90),
            Leaderboard.objects.create(user=users[2], score=95),
            Leaderboard.objects.create(user=users[3], score=85),
            Leaderboard.objects.create(user=users[4], score=80),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(
                name='Cycling Training',
                description='Training for a road cycling event'
            ),
            Workout.objects.create(
                name='Crossfit',
                description='Training for a crossfit competition'
            ),
            Workout.objects.create(
                name='Running Training',
                description='Training for a marathon'
            ),
            Workout.objects.create(
                name='Strength Training',
                description='Training for strength'
            ),
            Workout.objects.create(
                name='Swimming Training',
                description='Training for a swimming competition'
            ),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
