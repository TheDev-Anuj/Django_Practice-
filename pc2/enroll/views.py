from django.shortcuts import render
from enroll.models import Students
# Create your views here.
def index(request):
    stud = Students.objects.all()
    return render(request,'enroll/enrollone.html', {'stu': stud})