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

# about page function
def about_view(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'page-about.html',context)


# contact url function 
def contact_view(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'page-contact.html',context)

# Author url function
def author_view(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'page-author.html',context)

# 404 error page url function
def erre_404_view(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }
    return render(request,'page-404.html',context)






# single post show
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




# register or sign up
from django.contrib.auth.models import User
def register_view(request):
    # from register tamplte get data 
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Buildin user used and save data into database
        User.objects.create_user(username=username,email=email,password=password)

        # redirect into login page after save data into database
        return redirect('login_url_view')
    categories = category.objects.all()
    return render(request,'page-register.html',{'categories': categories})


# after completing registration now login function works
def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')

        # match this data information with database data
        user = authenticate(request,username=username,password=password)

        # check is everything ok or not
        if user is not None:
            # if match login
            login(request,user)
            # then direct Dashboard entry
            return redirect('dashboard_url_view')
        else:
            # login page a redirect
            return render(request,'page-login.html', {'error':'Wrong User Name and password'})
    
    categories = category.objects.all()
  
    # Otherwise return only login page
    return render(request,'page-login.html',{'categories': categories})

def category_view(request):
    categories = category.objects.all()
      
    # Otherwise return only login page
    return render(request,'category-list.html',{'categories': categories})

# Dashboard view create after successfully check login logic
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_url_view')
def dashboard_view(request):
    # request.user: who log in now
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_heading = request.POST.get('sub_heading')
        short_description = request.POST.get('short_description')
        detailed_description = request.POST.get('detailed_description')
        photo_click_by = request.POST.get('photo_click_by')
        author_image = request.FILES.get('author_image')
        post_image = request.FILES.get('post_image')
        thumbil_photo = request.FILES.get('thumbil_photo')
        
        # Save post into database
        Post.objects.create(
            author=request.user,
            title=title,
            sub_heading=sub_heading,
            short_description=short_description,
            detailed_description=detailed_description,
            photo_click_by=photo_click_by,
            author_image=author_image,
            post_image=post_image,
            thumbil_photo=thumbil_photo
        )
        return redirect(
            'dashboard_url_view'
        )
    # বর্তমান লগইন করা ইউজারের সব পোস্ট ডেটাবেজ থেকে ফিল্টার করে আনা
    user_posts = Post.objects.filter(author=request.user)
    context ={
        'Current_User': request.user,
        'posts': user_posts,

    }

    return render(request,'dashboard.html',context)