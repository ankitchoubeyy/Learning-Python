from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(req):
    msg = "Hello and welcome to first view"
    return HttpResponse(msg)

def about(req):
    text = "This is about page"
    return HttpResponse(text)

def contact(req):
    msg = "This is contact page"
    return HttpResponse(msg)


