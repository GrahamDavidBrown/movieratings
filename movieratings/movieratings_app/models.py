from django.db import models

# Create your models here.

# Create your models here.
class Movie(models.Model):
    movie_id = models.Integer
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=15)
    imdb_link = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)


class Rating(models.Model):
    rater_id = models.Integer
    movie_id = models.Integer
    rating = models.Integer
    timestamp = models.Integer


class Rater(models.Model):
    rater_id = models.Integer
    age = models.Integer
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.Integer
