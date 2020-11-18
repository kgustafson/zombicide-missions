from django.db import models
from django.utils import timezone


class Season(models.Model):
    season = models.CharField(max_length=100)
    def __str__(self):
        return self.season

class Tile(models.Model):
    tile = models.CharField(max_length=3)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    def __str__(self):
        return(self.tile + " " + self.season.season)

class Mission(models.Model):
    title = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    pdf_loc = models.CharField(max_length=100)
    title_id = models.CharField(max_length=100)
    num_players = models.CharField(max_length=100)
    length_play = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    tiles = models.ManyToManyField(Tile)
    seasons = models.ManyToManyField(Season)
    date_posted = models.DateTimeField(default=timezone.now)
    # author =  models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
