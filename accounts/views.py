from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .utils import send_welcome_sms
from ecommerce.models import category, product, order
from django.db.models import Sum, F

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-p', 'placeholder': 'Enter your username'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-p', 'placeholder': 'Your phone number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control-p', 'placeholder': '••••••••'}))
    captcha = CaptchaField()

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-p', 'placeholder': 'Username'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-p', 'placeholder': 'Mobile'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-p', 'placeholder': 'you@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control-p', 'placeholder': 'Password'}))
    captcha = CaptchaField()

from django.http import JsonResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

def refresh_captcha(request):
    """
    Refresh the CAPTCHA image via AJAX.
    """
    new_key = CaptchaStore.generate_key()
    new_image_url = captcha_image_url(new_key)
    return JsonResponse({
        'key': new_key,
        'image_url': new_image_url
    })

def Login(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home')

    if request.method == 'POST':
        # Check if the form was submitted from the modal (using 'modal' prefix) or the login page
        prefix = 'modal' if 'modal-username' in request.POST else None
        form = LoginForm(request.POST, prefix=prefix)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get('phone_number')

            # Authenticate username and password first
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Check if user has a profile
                try:
                    profile = user.profile
                    if profile.phone_number != phone_number:
                        messages.error(request, "Phone number does not match for this account.")
                        return render(request, 'login.html', {'form': form})
                except Profile.DoesNotExist:
                    # If user exists but has no profile (like a superuser), create it now
                    if Profile.objects.filter(phone_number=phone_number).exists():
                        messages.error(request, "This phone number is already linked to another account.")
                        return render(request, 'login.html', {'form': form})
                    
                    Profile.objects.create(user=user, phone_number=phone_number)
                
                # Login successful
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                
                # Redirect based on user role
                if user.is_superuser:
                    return redirect('admin_home')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            if 'captcha' in form.errors:
                messages.error(request, "Invalid CAPTCHA. Please try again.")
            else:
                messages.error(request, "Please correct the errors below.")
            
        return render(request, 'login.html', {'form': form})
    
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Register(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home')    

    if request.method == 'POST':
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        prefix = 'modal' if 'modal-username' in request.POST else None
        form = RegisterForm(request.POST, prefix=prefix)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone_number = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            if User.objects.filter(username=username).exists():
                if is_ajax:
                    return JsonResponse({'success': False, 'message': "Username already exists."})
                messages.error(request, "Username already exists.")
                return render(request, 'register.html', {'form': form})
            
            if Profile.objects.filter(phone_number=phone_number).exists():
                if is_ajax:
                    return JsonResponse({'success': False, 'message': "Phone number already registered."})
                messages.error(request, "Phone number already registered.")
                return render(request, 'register.html', {'form': form})

            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=user, phone_number=phone_number)
            
            # Send welcome SMS
            send_welcome_sms(phone_number, username)
            
            if is_ajax:
                return JsonResponse({
                    'success': True, 
                    'message': "Register successful",
                    'show_login': True
                })
            
            messages.success(request, "Register successful")
            return redirect('login')
        else:
            if is_ajax:
                if 'captcha' in form.errors:
                    return JsonResponse({'success': False, 'message': "Invalid CAPTCHA. Please try again."})
                return JsonResponse({'success': False, 'message': "Please correct the errors below."})
            
            if 'captcha' in form.errors:
                messages.error(request, "Invalid CAPTCHA. Please try again.")
            else:
                messages.error(request, "Please correct the errors below.")
            return render(request, 'register.html', {'form': form})
    
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def Logout(request):

    if not request.user.is_authenticated:
        messages.info(request, "You are not logged in.")
        return redirect('home')
    
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def admin_home(request):
    if not request.user.is_superuser:
        return redirect('admin_restricted')
    
    # Calculate Real-time stats
    total_products = product.objects.count()
    total_users = User.objects.count()
    
    # Revenue calculation (Price * Quantity)
    total_revenue = order.objects.annotate(
        item_total=F('product__price') * F('quantity')
    ).aggregate(Sum('item_total'))['item_total__sum'] or 0
    
    # Pending orders
    pending_orders = order.objects.count()
    
    context = {
        'total_products': total_products,
        'total_users': total_users,
        'total_revenue': total_revenue,
        'pending_orders': pending_orders,
    }
    return render(request, 'admin_home.html', context)

def add_product(request):
    if not request.user.is_superuser:
        return redirect('admin_restricted')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        is_featured = request.POST.get('is_featured') == 'on'

        if name and price and category_id and description and image:
            try:
                cat = category.objects.get(name__iexact=category_id)
                product.objects.create(
                    name=name,
                    price=price,
                    category=cat,
                    description=description,
                    image=image,
                    is_featured=is_featured
                )
                messages.success(request, f"Product '{name}' added successfully!")
                return redirect('add_product')
            except category.DoesNotExist:
                messages.error(request, "Selected category does not exist.")
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'add_product.html', {'categories': category.objects.all()})

def add_category(request):
    if not request.user.is_superuser:
        return redirect('admin_restricted')

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        is_featured = request.POST.get('is_featured') == 'on'

        if name and image:
            category.objects.create(name=name, image=image, is_featured=is_featured)
            messages.success(request, f"Category '{name}' created successfully!")
            return redirect('add_category')
        else:
            messages.error(request, "All fields are required.")
            
    return render(request, 'add_category.html', {'categories': category.objects.all()})
    


def admin_restricted(request):
    if not request.user.is_authenticated:
        messages.info(request, "You are not logged in.")
        return redirect('home')
    
    return render(request, 'admin_restricted.html')

    
