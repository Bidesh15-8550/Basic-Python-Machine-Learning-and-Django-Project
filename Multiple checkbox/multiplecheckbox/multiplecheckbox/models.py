from django.db import models

class colornames(models.Model):
    colorname= models.CharField(max_length=100)