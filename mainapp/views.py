from mainapp.models import Category
from .models import *
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    a = 3
    b = 5
    c = a+b
    return HttpResponse(a+b)

def second_page(request):
    return HttpResponse("SecondPage")

def example(request):
    return render(request, 'example.html')

def shop(request):
    return render(request, 'shop.html')

def shop_laptop(request):
    return render(request, 'shop_laptop.html')


def shop_console(request):
    return render(request, 'shop_console.html')


def shop_handphone(request):
    return render(request, 'shop_handphone.html')


def first_page(request):
    return render(request, 'firstpage.html')


def second_page(request):
    return render(request, 'secondpage.html')

def cobacoba(request):
    return render(request, 'cobacoba.html')

def shop_laptop_list(request):
    return render(request, 'shop_laptop_list.html')

def coba_list(request):
    try:
        print(request.GET)
        Category_laptop = Category.objects.get(pk=1)
        Product_laptop = Product.objects.filter(category=Category_laptop).filter(name__contains=request.GET['product_name'])
        #WHERE NAME like 'chrome'
        if(Product_laptop.count() != 0 ):
            return render(request, 'coba_list.html', {'product_list': Product_laptop, 'available': True})
        else:
            return render(request, 'coba_list.html', {'available': False})
    except:
        return HttpResponse("kalau error")
    


#def shop_makeover_list(request):
 #   try:    
  #      category_eyes = Category.objects.get(pk=1)
   #     product_makeup = Product.objects.filter(category=category_eyes)
    #    return render(request, 'shop_makeover_list.html', {'product_list': product_makeup})
    #except:
     #   return HttpResponse("Terjadi Error")