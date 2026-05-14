from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = get_user_model().objects.create(username="testuser")
        activity = Activity.objects.create(user=user, type="run", duration=30)
        self.assertEqual(activity.type, "run")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = get_user_model().objects.create(username="testuser2")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = get_user_model().objects.create(username="testuser3")
        workout = Workout.objects.create(user=user, name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")
        self.assertEqual(workout.description, "Do 20 pushups")
