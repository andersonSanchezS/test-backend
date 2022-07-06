from django.db import models

# Create your models here.


class cities(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)


class divisions(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)


class teams(models.Model):
    name = models.CharField(max_length=100)
    numberOfPlayers = models.IntegerField()
    city = models.ForeignKey(cities, on_delete=models.CASCADE)
    division = models.ForeignKey(divisions, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)


class players(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(teams, on_delete=models.CASCADE)
    age = models.IntegerField()
    salary = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    goals = models.IntegerField()
    played_matches = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)


class matches(models.Model):
    team1 = models.ForeignKey(
        teams, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(
        teams, on_delete=models.CASCADE, related_name='team2')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)


class positions(models.Model):
    teamId = models.ForeignKey(teams, on_delete=models.CASCADE)
    pj = models.IntegerField()
    pg = models.IntegerField()
    pe = models.IntegerField()
    pp = models.IntegerField()
    goals = models.IntegerField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_At = models.DateTimeField(null=True, blank=True)
