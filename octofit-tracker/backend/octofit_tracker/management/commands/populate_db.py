from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Usuń istniejące dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Dodaj drużyny
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Dodaj użytkowników
        users = [
            User(email='ironman@marvel.com', username='ironman', team=marvel),
            User(email='captain@marvel.com', username='captain', team=marvel),
            User(email='batman@dc.com', username='batman', team=dc),
            User(email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Dodaj aktywności
        Activity.objects.create(user=users[0], type='run', duration=30)
        Activity.objects.create(user=users[1], type='cycle', duration=45)
        Activity.objects.create(user=users[2], type='swim', duration=25)
        Activity.objects.create(user=users[3], type='run', duration=60)

        # Dodaj leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=110)
        Leaderboard.objects.create(user=users[3], points=120)

        # Dodaj treningi
        Workout.objects.create(user=users[0], name='Iron Endurance', description='Run 5km')
        Workout.objects.create(user=users[1], name='Shield Cycle', description='Cycle 10km')
        Workout.objects.create(user=users[2], name='Bat Swim', description='Swim 1km')
        Workout.objects.create(user=users[3], name='Super Run', description='Run 10km')

        # Tworzenie unikalnego indeksu na email
        with connection.cursor() as cursor:
            cursor.db_conn['users'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi.'))

# MODELE
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
