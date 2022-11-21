from django.shortcuts import render, redirect

# from .models import Task

def home(request):
    return render(request, 'main/home.html')
