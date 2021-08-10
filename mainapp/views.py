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
