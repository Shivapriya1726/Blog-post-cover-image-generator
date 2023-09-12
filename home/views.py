from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse
from django.forms.utils import ErrorDict




@login_required(login_url='login')
def home(request):
    username = request.user.username if request.user.is_authenticated else None
    context = {'username': username}
    return render(request,'home.html',context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return JsonResponse({'status': 'success'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})

    context = {'form': form}
    return render(request, 'signin.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse('error')
    return render(request, 'login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')