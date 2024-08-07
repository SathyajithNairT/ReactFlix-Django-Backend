from django.db import models

# Create your models here.


class ShowDataModel(models.Model):
    title = models.CharField(max_length= 1000)  
    grouping = models.CharField(max_length= 100, default= 'No Group')
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    overview = models.TextField()
    poster = models.URLField(max_length= 1000)
    banner = models.URLField(max_length= 1000)
    genre = models.CharField(max_length= 1000)

    def __str__(self):
        return self.title 
