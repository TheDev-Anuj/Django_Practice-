from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees(request):
    return render(request,'fees/feesone.html')