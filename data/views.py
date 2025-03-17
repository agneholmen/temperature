from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

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

def statistics_point(request, pk):
    point = Point.objects.get(id=pk)

    chart_data = get_data(pk, 8)

    return render(
        request,
        'data/point_diagram.html',
        {
            'chart_data': chart_data,
            'point': point
        }
    )

def statistics_point_data(request, pk, hours):
    return JsonResponse(get_data(pk, hours))

def get_data(point, hours):
    now = timezone.now()

    hours_ago = now - timezone.timedelta(hours=hours)

    measurements = Measurement.objects.filter(point=point, time__gte=hours_ago, time__lte=now).order_by('time')

    chart_data = {
        "y_data": [],
        "x_data": []
    }

    for measurement in measurements:
        chart_data["y_data"].append(measurement.temperature)
        chart_data["x_data"].append(measurement.time.strftime('%H:%M:%S'))

    return chart_data

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