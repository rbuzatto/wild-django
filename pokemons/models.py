from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    damage = models.BigIntegerField()
    special_damage = models.BigIntegerField()
    life_points = models.BigIntegerField()
