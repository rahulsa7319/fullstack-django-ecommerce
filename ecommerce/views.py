from django.shortcuts import render, redirect
from .models import product, order, category
from django.contrib.auth.models import User
from django.db.models import Sum, F

# Create your views here.

def Home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if not request.GET.get('view_front'):
            return redirect('admin_home')
            
    categories = category.objects.filter(is_featured=True)[:3]
    if not categories.exists():
        categories = category.objects.all()[:3]
        
    featured_products = product.objects.filter(is_featured=True)[:8]
    if not featured_products.exists():
        featured_products = product.objects.all()[:8]
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
        
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def shop_1(request):
    return render(request, 'shop_1.html')

def shop_2(request):
    return render(request, 'shop_2.html')

def shop_3(request):
    return render(request, 'shop_3.html')

def shop_4(request):
    return render(request, 'shop_4.html')

def shop_5(request):
    return render(request, 'shop_5.html')

def shop_6(request):
    return render(request, 'shop_6.html')

def shop_7(request):
    return render(request, 'shop_7.html')

def shop_8(request):
    return render(request, 'shop_8.html')

def shop_9(request):
    return render(request, 'shop_9.html')

def shop_10(request):
    return render(request, 'shop_10.html')

def shop_11(request):
    return render(request, 'shop_11.html')

def shop_12(request):
    return render(request, 'shop_12.html')

def contact(request):
    return render( request, 'contact.html')

def watch(request):
    return render(request, 'watch.html')

def watch_1(request):
    return render(request, 'watch_1.html')

def watch_2(request):
    return render(request, 'watch_2.html')   
   
def watch_3(request):
    return render(request, 'watch_3.html')   
   
def watch_4(request):
    return render(request, 'watch_4.html')    
  
def watch_5(request):
    return render(request, 'watch_5.html')   
   
def watch_6(request):
    return render(request, 'watch_6.html')  
    
def watch_7(request):
    return render(request, 'watch_7.html')    
  
def watch_8(request):
    return render(request, 'watch_8.html')      

def watch_9(request):
    return render(request, 'watch_9.html')  
    
def watch_10(request):
    return render(request, 'watch_10.html')   
   
def watch_11(request):
    return render(request, 'watch_11.html')    
  
def watch_12(request):
    return render(request, 'watch_12.html')      

def Shoes(request):
    return render(request,'shoes.html')

def Sunglass(request):
    return render(request,'sunglass.html')

def Dress(request):
    return render(request,'dress.html')

def Accessories(request):
    return render(request, 'Accessories.html')

def shoe_1(request):
    return render(request, 'shoe_1.html')

def shoe_2(request):
    return render(request, 'shoe_2.html')

def shoe_3(request):
    return render(request, 'shoe_3.html')

def shoe_4(request):
    return render(request, 'shoe_4.html')

def shoe_5(request):
    return render(request, 'shoe_5.html')

def shoe_6(request):
    return render(request, 'shoe_6.html')

def shoe_7(request):
    return render(request, 'shoe_7.html')

def shoe_8(request):
    return render(request, 'shoe_8.html')

def shoe_9(request):
    return render(request, 'shoe_9.html')

def shoe_10(request):
    return render(request, 'shoe_10.html')

def shoe_11(request):
    return render(request, 'shoe_11.html')

def runing_shoes(request):
    return render(request, 'runing_shoes.html')

def shoe_12(request):
    return render(request, 'shoe_12.html')

def acc_1(request):
    return render(request, 'acc_1.html')

def acc_2(request):
    return render(request, 'acc_2.html')

def acc_3(request):
    return render(request, 'acc_3.html')

def acc_4(request):
    return render(request, 'acc_4.html')

def acc_5(request):
    return render(request, 'acc_5.html')

def acc_6(request):
    return render(request, 'acc_6.html')

def acc_7(request):
    return render(request, 'acc_7.html')

def acc_8(request):
    return render(request, 'acc_8.html')

def acc_9(request):
    return render(request, 'acc_9.html')



