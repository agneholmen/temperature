from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from data.api.serializers import MeasurementSerializer
from data.models import Measurement

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [AllowAny]