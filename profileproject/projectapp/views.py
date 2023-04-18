from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projectapp.models import Profile

def profile(request):
    return render(request, 'profile.html')


def log_fun(request):
    return render(request,'login.html')



# def logdata_fun(request):
#     s1 = Student.objects.get(Stud_Name=request.session['name'])
#     user_name = request.POST['txtusername']
#     user_pswd = request.POST['txtpawd']
#     user1=authenticate(username = user_name,password = user_pswd)
#     if user1 is not None:
#         if user1.is_superuser:
#             return redirect('adminhome')
#
#
#     elif Student.objects.filter(Q(Stud_Name=user_name) & Q(Stud_pass=user_pswd)).exists():
#         request.session['name'] = user_name
#         return render(request, 'studenthome.html',{'data':s1})
#
#     else:
#         return render(request,'login.html',{'data':'User is not super user'})


def home(request):
    return render(request,'home.html')


def email(request):
    return render(request,'email.html')


def contact(request):
    return render(request,'contact.html')