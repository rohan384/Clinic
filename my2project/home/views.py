from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Departments, Doctors
from .forms import BookingForm

# from django.contrib.auth.models import User
# Create your views here.
# def login_view(request):
#     return render(request,'login.html')



def register_view(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('sucessfully registered')
            return redirect(reverse('register'))
    return render(request,'accounts/register.html',{'form':form})

# def loginn(request):
#     if request.method == "POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return HttpResponse('login')
#         else:
#             return redirect('signup.html')

#     return render(request,'login.html')



# def signup(request):
#     if request.method == "POST":
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         myuser=User.objects.create_user(username,email,password)
#         myuser.save()
#         return redirect('login')
#     return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def homeview(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html', dict_form)
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'dep.html', dict_dept)


