from django.db import models
from django.contrib.auth import get_user_model

class Team(models.Model):
    name = models.CharField(max_length=100)

class Activity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
