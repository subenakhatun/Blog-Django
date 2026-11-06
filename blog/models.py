from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    category = models.ForeignKey(category,on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True)

    # Slug auto genration
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{ self.category.name} -> {self.name}'

# postmodel
class Post(models.Model):
    title = models.CharField(max_length = 300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    author_image = models.ImageField(upload_to='author_pics/', blank=True, null=True)
    short_description = models.TextField(max_length = 500)
    highlight_description = models.TextField(blank=True, null=True)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    detailed_description = models.TextField()
    post_image = models.ImageField(upload_to="posts/")
    photo_click_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
    )

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
