from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.

# THINGS TO KEEP IN MIND
# Class: HttpResponse
# Each view function takes an HttpRequest object as its first parameter, which is typically named request.
# function: render
# return an HTML page

def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def contact_view(request):
    return render(request, "contact.html", {})

def data_view(request):
    my_content = {
        "my_text" : "This is a data page",
        "my_number": 10000,
        "my_list" : [10,15,20,25,100,1001, -100]
    }
    return render(request, "data.html", my_content)


def about_view(request):
    return render(request, "about.html")

def current_datetime_view(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, "datetime.html", now)
