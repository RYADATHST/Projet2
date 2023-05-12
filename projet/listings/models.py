from django.db import models

class Domain(models.Model):
    permutation= models.fields.CharField(max_length=10000)


# Create your models here.
