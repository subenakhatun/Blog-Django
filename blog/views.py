from django.db.models import F
from django.shortcuts import render,get_object_or_404
from .models import category,SubCategory,Post,Comment,Subscriber
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'index.html',context)

def single_post_view(request, pk):
  Post.objects.filter(pk=pk).update(views_count=F("views_count") + 1)
  post = get_object_or_404(Post, pk=pk)

  comments = post.comments.filter(parent__isnull=True)

  author_other_posts = Post.objects.filter(author=post.author).exclude(pk=pk)
  manucategory = category.objects.all()
  subscriber = Subscriber.objects.all()
  
  context = {
      "post": post,
      "comments": comments,
      "author_other_posts": author_other_posts,
      'categories': manucategory,
      'subscriber':subscriber,
      
      
  }
  return render(request, "single.html", context)

