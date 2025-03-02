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

def statistics_point(request, point_id):
    measurements = Measurement.objects.filter(point=point_id).order_by('time')[:10]

    point = Point.objects.get(id=point_id)

    chart_data = {
        'y_data': [],
        'x_data': []
    }

    for measurement in measurements:
        chart_data['y_data'].append(measurement.temperature)
        chart_data['x_data'].append(measurement.time.strftime('%H:%M:%S'))

    return render(
        request,
        'data/point_diagram.html',
        {
            'chart_data': chart_data,
            'point': point
        }
    )

def get_latest_temperatures():
    temperatures = []

    for point in Point.objects.all():
        if Measurement.objects.filter(point=point).exists():
            measurement = Measurement.objects.filter(point=point).latest('time')
            temperatures.append({
                            'temperature': measurement.temperature, 
                            'time': measurement.time,
                            'point': point.name,
                            'point_id': point.id
                            })

    return temperatures