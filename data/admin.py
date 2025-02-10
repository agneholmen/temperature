from django.contrib import admin

from .models import Point, Temperature

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['point', 'temperature', 'time']