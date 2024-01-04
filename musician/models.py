from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_number = models.IntegerField()
    Instrument_type = models.TextField()

    def __str__(self) :
        return self.First_Name
