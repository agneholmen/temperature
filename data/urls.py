from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/point/<int:point_id>/', views.statistics_point, name='statistics_point'),
]