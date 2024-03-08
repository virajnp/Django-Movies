from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movies(models.Model):
    title = models.IntegerField()
    release_year = models.IntegerField()
    numbers_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
