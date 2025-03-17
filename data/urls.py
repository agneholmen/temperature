from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('statistics/', views.statistics, name='statistics'),
    path('statistics/point/<int:pk>/', views.statistics_point, name='statistics_point'),
    path('statistics/point/<int:pk>/data/<int:hours>/', views.statistics_point_data, name='statistics_point_data'),
]