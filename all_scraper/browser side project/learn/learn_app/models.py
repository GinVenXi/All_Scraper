# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    region = models.SmallIntegerField(max_length=30)
    type = models.SmallIntegerField(max_length=30)
    value = models.CharField(max_length=30)