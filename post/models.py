from django.db import models
from django.utils import timezone


# Create your models here.
class Posteo(models.Model):
	name=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	email=models.AutoF
	created_date=
