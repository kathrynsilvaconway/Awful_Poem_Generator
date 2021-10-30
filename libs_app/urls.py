from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('process_lib', views.process_lib),
    path('display_lib', views.display_lib)
]
