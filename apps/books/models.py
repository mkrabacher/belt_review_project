# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name='books')

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, related_name='reviews_given')
    book = models.ForeignKey(Book, related_name='reviews')