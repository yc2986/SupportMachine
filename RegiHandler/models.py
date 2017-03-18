from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

"""
according to stackoverflow post: 
http://stackoverflow.com/questions/25024795/django-1-7-where-to-put-the-code-to-add-groups-programatically
use this signal receiver to initialize database state
"""
@receiver(post_migrate)
def init_groups(sender, **kwargs):
    # design permission group
    try: 
        add_perm = Permission.objects.get(codename = 'add_group')
        change_perm = Permission.objects.get(codename = 'change_group')
        delete_perm = Permission.objects.get(codename = 'delete_group')
        # client
        client, created = Group.objects.get_or_create(name='client')
        client.save() 
        # admin
        admin, created = Group.objects.get_or_create(name='admin')
        admin.permissions.add(add_perm, change_perm, delete_perm)
        admin.save()
    except Permission.DoesNotExist:
        pass

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
    