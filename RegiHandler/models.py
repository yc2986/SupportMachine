from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class DolbyUser(models.Model):
    # point to already existed built-in django user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # company name, mandatory
    company = models.CharField(max_length = 100)
    # registration code, need to verify validation rule
    registration_code = models.CharField(max_length = 30)
    # phone number
    phone_number = models.CharField(max_length = 20)
    