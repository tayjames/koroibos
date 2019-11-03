from django.db import models

# Create your models here.
class Olympian(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    games = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    medal = models.CharField(max_length=255, default="", editable=False)

    def __repr__(self):
        '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.name, self.sex, self.age, self.height, self.weight, self.team, self.games, self.sport, self.event, self.medal)
