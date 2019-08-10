# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Tweaktalent(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    course = models.CharField(max_length=20)
    timings = models.CharField(max_length=120,blank=False)

    def __str__(self):
        return self.title
