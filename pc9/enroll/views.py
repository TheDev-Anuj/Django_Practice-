from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import User
# Create your views here.

def showuser(request):
    if request.method == 'POST':
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data.get('name')
            em = fm.cleaned_data.get('email')
            pw = fm.cleaned_data.get('password')
            reg = User(name = nm, email = em, password = pw)
            reg.save()
    else:
        fm = UserRegistrationForm()
        
    return render(request, 'enroll/noname.html', {'form':fm})