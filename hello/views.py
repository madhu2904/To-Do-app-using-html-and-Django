from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/base.html")
def brian(request):
    return HttpResponse("Hello ,brian")
def greet(request,name):
    return render(request,"hello/greet.html",{"name":name.capitalize()})
