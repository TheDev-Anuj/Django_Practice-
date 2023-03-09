from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def ShowUserData(request):
    if request.method=='POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            print('Form validated...!!!')
    else: 
        fm = UserRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
