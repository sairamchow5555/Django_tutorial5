from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s="<h1>Hello students welcome to Django class</h1>"
    return HttpResponse(s)
