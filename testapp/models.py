from django.db import models

class Count(models.Model):
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
