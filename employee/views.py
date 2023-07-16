from email.mime import image
from django.shortcuts import render, redirect
from employee import models
from . models import Employee, Department, Slider
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pathlib import Path
import os
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


# Create your views here.

def add(request):
    dept = Department.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        edu = request.POST['edu']
        prol = request.POST['prol']
        age = request.POST['age']
        gender = request.POST['gender']
        exsalary = request.POST['exsalary']
        deptname = request.POST['deptname']
        about = request.POST['about']
        image = request.FILES['image']
        employee = Employee(name=name, edu=edu, prol=prol, age=age, gender=gender,
                            exsalary=exsalary, deptname=deptname, about=about, image=image)
        employee.save()
        messages.success(request, 'Record created successful')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html', {'dept': dept})


def edit(request, id):
    prod = Employee.objects.get(id=id)
    department = Department.objects.all()

    if request.method == "POST":
        prod.name = request.POST.get('name')
        prod.edu = request.POST.get('edu')
        prod.prol = request.POST.get('prol')
        prod.age = request.POST.get('age')
        prod.gender = request.POST.get('gender')
        prod.exsalary = request.POST.get('exsalary')
        prod.deptname = request.POST.get('deptname')
        prod.about = request.POST.get('about')
        if len(request.FILES)!=0:
            if len(prod.image)>0:
                os.remove(prod.image.path)
            prod.image=request.FILES['image']
        prod.save()
        return redirect('/')
    else:
        context = {
            'prod': prod,
            'dept': department,
        }
        return render(request, 'update.html', context)


def view(request, id):
    id = Employee.objects.get(id=id)
    return render(request, 'view.html', {'data': id})


def admin(request):
    if request.user.is_authenticated:
        if 'search' in request.GET:
            search = request.GET['search']
            manage = Employee.objects.filter(name__icontains=search)
            if len(manage)!=0:
                pass
            else:
                manage = Employee.objects.all().order_by('-id')
        else:
            manage = Employee.objects.all().order_by('-id')
        slide = Slider.objects.all()
        context = {
        'emp': manage,
        'slide': slide,
        }
        return render(request, 'admin_tasks.html', context)

    else:
        return redirect('login')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    if len(employee.image) > 0:
        os.remove(employee.image.path)
    employee.delete()
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "invalid credentials")
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #
        if len(username) > 10:
            messages.error(request, "username should be in 10 characters")
            return HttpResponseRedirect('.')

        if password != cpassword:
            messages.error(request, "passwords are not matching")
            return HttpResponseRedirect('.')

        myuser = User.objects.create_user(username, email, password)
        myuser.fname = fname
        myuser.lname = lname
        myuser.save()
        messages.success(request, 'User created successfully')
        return HttpResponseRedirect('.')

    return render(request, 'register.html')


# slider codes

def slider(request):
    slider = Slider.objects.all()
    context = {
        'slider': slider,
    }
    if request.method == 'POST':
        image = request.FILES['img']
        slider = Slider(img=image)
        slider.save()
        return HttpResponseRedirect('/')
    return render(request, 'addcaro.html', context)


def delslider(request, id):
    slider = Slider.objects.get(id=id)
    if len(slider.img) > 0:
        os.remove(slider.img.path)
    slider.delete()

    return HttpResponseRedirect('/')
