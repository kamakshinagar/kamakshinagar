from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
import hello.logic

from .models import Greeting

# Create your views here.
#def index(request):
    # return HttpResponse('Hello from Python!')
    #return render(request, "index.html")

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)

def rc(request):
    print("I am working here")
    req = request.POST.get('req',200)
    dyno = request.POST.get('dyno',1)
    print(req)
    print(dyno)
    hello.logic.main_function(req,dyno)
    #print(request.POST)
    return render(request, "rc.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
   
    return render(request, "db.html", {"greetings": greetings})
