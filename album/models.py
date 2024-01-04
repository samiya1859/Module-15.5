from django.db import models
from musician.models import MusicianModel
# Create your models here.

ratings = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=1, choices=ratings)

    def __str__(self):
        return self.Album_name