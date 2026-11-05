from django.db import models
from django.utils.text import slugify

# Create your models here.
'''
Create category class. name with slug. then set slug if not given get from auto
then using str function catogry name show as name set.
then resiger category with admin.py
'''
class category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True)

    # Slug auto genration
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Subcategory
class SubCategory(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True)

    # Slug auto genration
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{ self.category.name} -> {self.name}'