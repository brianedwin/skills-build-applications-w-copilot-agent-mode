from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "thundergod", "password": "thundergodpassword"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "metalgeek", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "zerocool", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "email": "crashoverride@hmhigh.edu", "name": "crashoverride", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "sleeptoken", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        blue_team = {"_id": ObjectId(), "name": "Blue Team", "members": [u["_id"] for u in users[:3]]}
        gold_team = {"_id": ObjectId(), "name": "Gold Team", "members": [u["_id"] for u in users[3:]]}
        db.teams.insert_many([blue_team, gold_team])

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "type": "Cycling", "duration": 60, "date": datetime.now()},
            {"_id": ObjectId(), "user": users[1]["_id"], "type": "Crossfit", "duration": 120, "date": datetime.now()},
            {"_id": ObjectId(), "user": users[2]["_id"], "type": "Running", "duration": 90, "date": datetime.now()},
            {"_id": ObjectId(), "user": users[3]["_id"], "type": "Strength", "duration": 30, "date": datetime.now()},
            {"_id": ObjectId(), "user": users[4]["_id"], "type": "Swimming", "duration": 75, "date": datetime.now()},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
