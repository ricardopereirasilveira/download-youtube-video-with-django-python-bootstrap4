from django.db import models

class Download(models.Model):
    link = models.URLField()
