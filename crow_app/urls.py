from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_post', views.create_post),
    path('archives', views.archives),
    path('updoot', views.updoot),
    path('logout', views.logout),
]
