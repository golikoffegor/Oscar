from django.urls import path
from . import views

from .views import CoefficientView, ResultsView

urlpatterns = [
    path('', views.mat_vvoda, name = 'mat_vvoda'),
    path('coefficients/', CoefficientView.as_view()),
    path('coefficients/<int:pk>', CoefficientView.as_view()),
    path('results/', ResultsView.as_view()),
    path('results/<int:pk>', ResultsView.as_view()),
]
