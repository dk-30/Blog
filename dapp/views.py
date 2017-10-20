from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import *
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')

def password(request):
    user=request.user
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
            form=PasswordChangeForm(user)
    return render(request, 'password.html',{'form':form})


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=UserCreationForm()
    return render(request,'register.html', {'form':form})

def check(request):
    usern = request.POST['username']
    passn = request.POST['password']
    user = auth.authenticate(username=usern, password=passn)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request, 'invalid.html')

def profile(request):
    n=blog.objects.all()
    return render(request, 'profile.html', {'n':n})

def profile1(request,k):
    n=User.objects.get(id=k)
    j=blog.objects.all()
    return render(request,'profile1.html',{'n':n,'j':j})

def index(request):
    if request.user.is_authenticated():
        if request.method=='POST':
            form=dform(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.username = request.user
                f.save()
                return HttpResponseRedirect('/index/')
        else:
            form=dform()
        n=blog.objects.all()
        return render(request, 'index.html',{'n': n,'form': form,'f':request.user.username})
    else:
        return HttpResponseRedirect('/')

def friends(request):
    n=User.objects.all()
    n = n.exclude(id=request.user.id)
    return render(request, 'friends.html', {'n':n})

def delete(request,k):
    c = blog.objects.get(id=k)
    c.delete()
    return HttpResponseRedirect('/index/')

def edit(request,l):
    c = blog.objects.get(id=l)
    if request.method == 'POST':
        form = dform(request.POST,request.FILES,instance=c)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = dform(instance=c)

    return render(request, 'edit.html', {'form':form})



def search(request):
    if request.method == 'POST':
        s = request.POST['search_box']
        if s:
            ss = blog.objects.filter(caption__icontains=s)
            if ss:
                return render(request, 'search.html', {'t':ss})
            else:
                return render(request, 'not_found.html')
    else:
        return HttpResponseRedirect('/index/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


