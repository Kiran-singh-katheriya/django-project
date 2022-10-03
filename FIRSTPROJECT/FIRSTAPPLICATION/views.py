from urllib import request
from Django-project.FIRSTPROJECT.FIRSTAPPLICATION.models import Employee
from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h4>Welcome! to my Page!!</h4>")

def displayTemplate(request):
    return render(request,'tempApp/temp.html')

def modelPage(request):
    all_data=Employee.objects.all()
    print(all_data)
    return render(request,'FIRSTAPPLICATION)',context=all_data)
