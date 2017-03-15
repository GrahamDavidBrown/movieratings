from django.db import models



# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=15)
    imdb_link = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def get_avg_rating(movie_id):
        all_ratings = Rating.objects.filter(movie_id).Rating
        return sum(all_ratings) / len(all_ratings)
        # figure out correct iterable for get_avg_ratings
    def get_top_n_movies_by_rating():
        pass


class Rating(models.Model):
    rater_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()


class Rater(models.Model):
    rater_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.IntegerField()

    def get_top_n_unseen_movies():
        pass

    def get_total_avg_ratings():
        pass
