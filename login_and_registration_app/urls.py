from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('success', views.success),
    path('log_out', views.log_out),
]
