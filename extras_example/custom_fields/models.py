# -*- coding: utf-8 -*-
from django_extras.db import models


class Example(models.Model):
    price = models.MoneyField()

