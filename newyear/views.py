from django.shortcuts import render

# Create your views here.
import datetime

def index(request):
    now=datetime.datetime.now()
    return render(request,"newyear/base.html",{"newyear":now.month==1 and now.day==1})
