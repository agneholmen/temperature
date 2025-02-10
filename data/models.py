from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Temperature(models.Model):
    temperature = models.FloatField(blank=False)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    time = models.DateTimeField()