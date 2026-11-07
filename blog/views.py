from django.db.models import F
from django.shortcuts import render,get_object_or_404
from .models import category,SubCategory,Post,Comment,Subscriber
from django.contrib.auth import login
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'index.html',context)

def single_post_view(request, pk):
  # ১. নির্দিষ্ট পোস্টটি ডাটাবেজ থেকে আনা এবং ভিউ কাউন্ট ১ বাড়িয়ে দেওয়া
  Post.objects.filter(pk=pk).update(views_count=F("views_count") + 1)
  post = get_object_or_404(Post, pk=pk)

  # ২. এই পোস্টের আন্ডারে যত মেইন কমেন্ট আছে সেগুলোর লিস্ট
  comments = post.comments.filter(parent__isnull=True)

  # ৩. লেখকের অন্য সব পোস্টের লিস্ট (বর্তমান পোস্ট বাদে)
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

from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    # ১. পাসওয়ার্ড মিলছে কি না চেক করা
    if password != confirm_password:
      return render(
          request,
          'page-register.html',
          {'error': 'Password and Confirm Password do not match!'},
      )

    # ২. ইউজারনেম আগে থেকে আছে কি না চেক করা
    if User.objects.filter(username=username).exists():
      return render(
          request, 'page-register.html', {'error': 'Username already exists!'}
      )

    # ৩. নতুন ইউজার তৈরি ও ডেটাবেজে সেভ করা
    User.objects.create_user(
        username=username, email=email, password=password
    )

    # ৪. সফলভাবে রেজিস্টার হলে লগইন পেজে রিডাইরেক্ট করবে
    return redirect('login')

  return render(request, 'page-register.html')