from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Measurement, Point

def home(request):
    return render(
        request,
        'data/home.html'
    )

def statistics(request):
    temperatures = get_latest_temperatures()

    return render(
        request,
        'data/statistics.html',
        {'temperatures': temperatures}
    )

def get_latest_temperatures():
    temperatures = []

    for point in Point.objects.all():
        if Measurement.objects.filter(point=point).exists():
            measurement = Measurement.objects.filter(point=point).latest('time')
            temperatures.append({
                            'temperature': measurement.temperature, 
                            'time': measurement.time,
                            'point': point.name
                            })

    return temperatures