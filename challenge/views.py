from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jan(request):
    return HttpResponse("This works!")
def feb(request):
    return HttpResponse("hey we are now in february month")