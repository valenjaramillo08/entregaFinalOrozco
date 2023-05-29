from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':

        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            return
        else:
            messages.error(request, 'Password no hace match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
def login(request):
    if request.method == 'POST':
        # login de usuarios
        pass
    else:
        return render(request, 'accounts/login.html')
def logout():
    return redirect('index')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')