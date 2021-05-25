from django.db import models

"""
creating models and Category to record 
"""
class Category(models.Model):
    name= models.CharField(max_length=255,db_index=True)
"""
in order to get the catogory need to type the slug

"""
slug= models.SlugField(max_length=255,unique=True)

"""
 meta data ,data about deta more details abbout data
"""
class Meta:
    verbose_name_plural = 'catagories'

