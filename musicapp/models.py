from email.policy import default
from django.db import models
from datetime import date

# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return(self.first_name)

 
class Song (models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=date.today)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return (self.title)
    

class Lyrics (models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return(self.song_id)
        