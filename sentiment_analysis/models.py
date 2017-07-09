from django.db import models


class Data(models.Model):
    date = models.DateTimeField()
    happy = models.IntegerField()
    love = models.IntegerField()
    hopeful = models.IntegerField()
    neutral = models.IntegerField()
    angry = models.IntegerField()
    hopeless = models.IntegerField()
    hate = models.IntegerField()
    sad = models.IntegerField()
