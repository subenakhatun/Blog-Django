from django.shortcuts import render
from .models import category,SubCategory

# Create your views here.
def home(request):
    manucategory = category.objects.all()
    context ={
        'categories': manucategory,
        
    }




    return render(request,'index.html',context)
