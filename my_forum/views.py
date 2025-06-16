from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def user_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        dup_user = User.objects.filter(username=username).exists()
        if dup_user:
            messages.error(request, 'username already exists')
            return redirect('user_profile')
        else:
           query_set = User.objects.create_user(first_name=first_name,
                                                      last_name=last_name,
                                                      username=username,
                                                      email=email ,
                                                      password=password,
                                                 )
    
           query_set.save()
           messages.success(request, 'Account Created Successfully')
           return redirect('user_profile')

    return render(request, 'registration_page.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(username=username, password=password)
        if user:
           login(request, user)
           return redirect('main')
        else:
            messages.error(request, 'Please Create Account')
            return redirect('login_user')
    return render(request, 'login.html')


def main(request): 
    if request.method == 'POST':
        tasks = request.POST.get('tasks')
        user = request.user
        query_set = Task.objects.create(tasks=tasks, user=user)
        query_set.save()
        return redirect('main')
    
    data = Task.objects.filter(user=request.user)
    data2 = User.objects.filter(username=request.user)
    context = {'data':data, 'data2':data2}
    return render(request, 'main_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_user')

