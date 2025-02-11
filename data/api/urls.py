from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'data'

router = routers.DefaultRouter()
router.register('data', views.MeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
