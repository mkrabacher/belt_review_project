# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from datetime import *


# class UserManager(models.Manager):
#     def validate(self, postData):
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         errors = {}

#         if len(postData['fName']) < 2:
#             errors['fName'] = 'You gotta have a longer first name, bruh.'
#         if len(postData['lName']) < 2:
#             errors['lName'] = 'You gotta have a longer last name, bruh.'
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = 'You gotta have a valid email, bruh.'
#             errors['email2'] = 'Try regular chars followed by an @ followed by regular chars followed by a dot followed by regular chars'
#         if datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.now():
#             errors['birthday'] = "That date hasn't happen yet. So wtf are you doing puttin it in as your b-day. "
#         if postData['password'] != postData['pw_conf']:
#             errors['passwordMatch'] = 'You gotta have a longer last name, bruh.'
#         if len(postData['password']) < 8:
#             errors['password'] = 'You gotta have a longer pw, bruh.'

#         return errors

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # objects = UserManager()
