from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.

# 1. Category Model
class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Slug auto genration
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# 2. SubCategory Model
class SubCategory(models.Model):
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, related_name='subcategories'
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Slug auto genration
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category.name} -> {self.name}'


# 3. Tag Model (এখানে slug এ blank=True এবং save method যোগ করা হয়েছে)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# 4. Photographer Model
class Photographer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='photographers/', blank=True, null=True
    )

    def __str__(self):
        return self.name


# 5. Post Model
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    author_image = models.ImageField(
        upload_to='author_pics/', blank=True, null=True
    )
    short_description = models.TextField(max_length=500)
    highlight_description = models.TextField(blank=True, null=True)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    detailed_description = models.TextField()
    post_image = models.ImageField(upload_to='posts/')
    photo_click_by = models.CharField(max_length=100, blank=True, null=True)
    thumbil_photo = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    category = models.ForeignKey(
        category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        if self.category:
         return f'[{self.category.name}] {self.title}'
        return self.title


# 6. Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # সেলফ-রেফারেন্সিং প্যারেন্ট (রিপ্লাই হ্যান্ডেল করার জন্য)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
    )

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'


# 7. Subscriber Model
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email