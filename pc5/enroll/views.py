from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def Studentdata(request):
    fm = StudentRegistrationForm()
    return render(request, 'enroll/stuinfo.html', {'form': fm})
