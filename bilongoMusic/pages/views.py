from django.shortcuts import render
from django.http import HttpResponse
from writers.models import Writer

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def about(request):
    writers = Writer.objects.order_by('fecha_nacimiento')
    context = {'writers': writers}
    return render(request, 'pages/about.html', context)
def contact(request):
    return render(request, 'pages/contact.html')