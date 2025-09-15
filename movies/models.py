from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movies(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre,on_delete=models.PROTECT,related_name='movies')
    actors = models.ManyToManyField(Actor)
    realease_date = models.DateField(null=True,blank=True)
    resume = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title
    
