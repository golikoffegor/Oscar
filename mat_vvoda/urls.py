from django.urls import path
from . import views

urlpatterns = [
    path('', views.mat_vvoda, name = 'mat_vvoda')
]