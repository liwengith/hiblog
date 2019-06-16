#from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    cnotent = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

# class Meta:
# 	"""docstring for Meta"""
# 	db_table = 'Blog'