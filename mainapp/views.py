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


    
