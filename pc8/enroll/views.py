from django.shortcuts import render
from .forms import data
# Create your views here.
def showformdata(request):
    if request.method=='POST':
        fm = data(request.POST)
        if fm.is_valid():
            print('Form validated...!!!')
    else: 
        fm = data()
    return render(request, 'enroll/noname.html', {'form':fm})

    
