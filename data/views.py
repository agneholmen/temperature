from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(
        request,
        'data/home.html'
    )

def statistics(request):
    return render(
        request,
        'data/statistics.html'
    )