from django.contrib import admin

# Register your models here.

from .models import category,SubCategory,Post,Comment,Subscriber

admin.site.register(category)
admin.site.register(SubCategory)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subscriber)
