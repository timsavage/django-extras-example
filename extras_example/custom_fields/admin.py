# -*- coding: utf-8 -*-
from django.contrib.admin import site
from extras_example.custom_fields.models import Example


site.register(Example)
