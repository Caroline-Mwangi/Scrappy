from django.db import models

# Create your models here.
class Tweets(models.Model):
    search_tag = models.CharField(max_length=100)
    tweet = models.CharField(max_length=10000)
    date = models.DateTimeField()