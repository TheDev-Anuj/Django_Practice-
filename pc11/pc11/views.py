from django.http import HttpResponse
from django.shortcuts import render

def set(request):
    res = HttpResponse('cookie set...')
    res.set_cookie('name', 'anuj')
    res.set_cookie('lname', 'tiwari')


    return res

def get(request):
    print(request.COOKIES)
    return HttpResponse(str(request.COOKIES))