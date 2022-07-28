from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=255)
    nim = models.IntegerField(max_length=10)
    jurusan = models.CharField(max_length=255)
