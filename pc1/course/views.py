from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(request):
    nm = {'nm': 'Anuj'}
    return render(request,'course/courseone.html', nm)
