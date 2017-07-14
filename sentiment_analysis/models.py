from django.db import models


class Data(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    happy = models.FloatField()
    love = models.FloatField()
    hopeful = models.FloatField()
    neutral = models.FloatField()
    angry = models.FloatField()
    hopeless = models.FloatField()
    hate = models.FloatField()
    sad = models.FloatField()
