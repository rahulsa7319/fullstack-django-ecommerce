"""
URL configuration for Resell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ecommerce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),          # homepage         # homepage
    path('about/', views.about, name='about'),  # register page  # register page
    path('contact/', views.contact, name='contact'), 
    path('shop/', views.shop, name='shop'),

    path('shop_1/', views.shop_1, name='shop_1'),
    path('shop_2/', views.shop_2, name='shop_2'),
    path('shop_3/', views.shop_3, name='shop_3'),
    path('shop_4/', views.shop_4, name='shop_4'),
    path('shop_5/', views.shop_5, name='shop_5'),
    path('shop_6/', views.shop_6, name='shop_6'),
    path('shop_7/', views.shop_7, name='shop_7'),
    path('shop_8/', views.shop_8, name='shop_8'),
    path('shop_9/', views.shop_9, name='shop_9'),
    path('shop_10/', views.shop_10, name='shop_10'),
    path('shop_11/', views.shop_11, name='shop_11'),
    path('shop_12/', views.shop_12, name='shop_12'),
    
    
    path('watch/', views.watch, name='watch'),
    path('watch_1/', views.watch_1, name='watch_1'),
    path('watch_2/', views.watch_2, name='watch_2'),
    path('watch_3/', views.watch_3, name='watch_3'),
    path('watch_4/', views.watch_4, name='watch_4'),
    path('watch_5/', views.watch_5, name='watch_5'),
    path('watch_6/', views.watch_6, name='watch_6'),
    path('watch_7/', views.watch_7, name='watch_7'),
    path('watch_8/', views.watch_8, name='watch_8'),
    path('watch_9/', views.watch_9, name='watch_9'),
    path('watch_10/', views.watch_10, name='watch_10'),
    path('watch_11/', views.watch_11, name='watch_11'),
    path('watch_12/', views.watch_12, name='watch_12'),
    path('shoes/', views.Shoes, name='shoes'),
    path('sunglass/', views.Sunglass, name='sunglass'),
    path('accessories/', views.Accessories, name='accessories'),

    path('shoe_1/', views.shoe_1, name='shoe_1'),
    path('shoe_2/', views.shoe_2, name='shoe_2'),
    path('shoe_3/', views.shoe_3, name='shoe_3'),
    path('shoe_4/', views.shoe_4, name='shoe_4'),
    path('shoe_5/', views.shoe_5, name='shoe_5'),
    path('shoe_6/', views.shoe_6, name='shoe_6'),
    path('shoe_7/', views.shoe_7, name='shoe_7'),
    path('shoe_8/', views.shoe_8, name='shoe_8'),
    path('shoe_9/', views.shoe_9, name='shoe_9'),
    path('shoe_10/', views.shoe_10, name='shoe_10'),
    path('shoe_11/', views.shoe_11, name='shoe_11'),
    path('shoe_12/', views.shoe_12, name='shoe_12'),
    
    path('runing_shoes/', views.runing_shoes, name='runing_shoes'),

    path('acc_1/', views.acc_1, name='acc_1'),
    path('acc_2/', views.acc_2, name='acc_2'),
    path('acc_3/', views.acc_3, name='acc_3'),
    path('acc_4/', views.acc_4, name='acc_4'),
    path('acc_5/', views.acc_5, name='acc_5'),
    path('acc_6/', views.acc_6, name='acc_6'),
    path('acc_7/', views.acc_7, name='acc_7'),
    path('acc_8/', views.acc_8, name='acc_8'),
    path('acc_9/', views.acc_9, name='acc_9'),

     path('accounts/', include('accounts.urls'), name='accounts'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
