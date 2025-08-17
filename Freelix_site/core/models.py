from django.db import models
import uuid

class Movies(models.Model):
    Genre_Choices = [
        ('action', 'Action'),
        ('comdedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror','Horror'),
        ('romance', 'Romance')

    ]

    uu_id = models.UUIDField(default = uuid.uuid4)
    title = models.CharField(max_length = 225)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length = 100, choices = Genre_Choices)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to = 'movie_images/')
    image_cover = models.ImageField(upload_to = 'movie_images/')
    video = models.FileField(upload_to = 'movie_videos/')
    movie_views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
    # Create your models here.
