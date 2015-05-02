from django.db import models
# Create your models here.

class Dataset(models.Model):
    docid = models.IntegerField()
    headline = models.TextField()
    trailText = models.TextField()
    byline = models.TextField()
    body = models.TextField()
    webURL = models.TextField()
    published= models.DateTimeField()
    imageLink = models.TextField()
    tags = models.TextField()
    section = models.TextField()
    clicks = models.IntegerField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class Hot(models.Model):
    docid=models.IntegerField()
    published=models.DateTimeField()
    hottness=models.FloatField()

