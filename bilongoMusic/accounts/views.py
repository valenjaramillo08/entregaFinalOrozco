from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        # registro de usuarios
        pass
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