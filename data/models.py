from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Measurement(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    temperature = models.FloatField(blank=False)
    time = models.DateTimeField()