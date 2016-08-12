from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Menus(models.Model):
    name=models.CharField(max_length=40)
    cost=models.IntegerField()
    hotel=models.ForeignKey(Restaurant)
    type=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
