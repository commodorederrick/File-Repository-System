from multiprocessing import context
from turtle import up
from django.shortcuts import render, redirect
from .forms import personForm
from .forms import uploadForm
from Dashboard.models import person
from Dashboard.models import upload
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'POST':
        form = personForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard-login')
    else:
        form = personForm()

    form = personForm()
    context = {
        'form': form,
    }
    return render(request, 'main/signup.html', context)


def login(request):
    return render(request, 'main/login.html')


def index(request):
    return render(request, 'main/index.html')


def pdf(request):
    data = upload.objects.all()

    context = {
        'data': data,
    }
    return render(request, 'main/pdf.html',context)


def uploadfunc(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Dashboard-index')
    form = uploadForm()
    context = {
        'form': form,
    }
    return render(request, 'main/upload.html', context)

def Journalfunc(request):
    files = journals.objects.all()

    context = {
        'files': files,
    }
    return render(request, 'main/journals.html', context)
