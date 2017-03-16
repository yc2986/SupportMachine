from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# email field force unique
User._meta.get_field('email').__dict__['_unique'] = True
# optional field allow null
User._meta.get_field('first_name').__dict__['null'] = True
User._meta.get_field('last_name').__dict__['null'] = True

class DolbyUser(models.Model):
    # point to already existed built-in django user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # company name, mandatory
    company = models.CharField(max_length = 100)
    # registration code, need to verify validation rule
    registration_code = models.CharField(max_length = 30)
    # phone number
    phone_number = models.CharField(max_length = 20)
    