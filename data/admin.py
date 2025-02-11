from django.contrib import admin

from .models import Point, Measurement

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['point', 'temperature', 'time']