from rest_framework import serializers
from data.models import Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['point', 'temperature', 'time']