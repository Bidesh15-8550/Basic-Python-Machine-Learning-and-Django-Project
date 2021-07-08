from django.db import models

class colornames(models.Model):
    colorname= models.CharField(max_length=100)
    class Meta:
        db_table="colors"