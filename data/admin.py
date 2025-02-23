from django.contrib import admin

from .models import Point, Measurement

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'point', 'temperature', 'time']