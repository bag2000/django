from django.urls import path

from measurement.views import Sens, Measur

urlpatterns = [
    path('sensors/', Sens.as_view()),
    path('sensors/<int:pk>/', Sens.as_view()),
    path('measurements/', Measur.as_view()),
    path('measurements/<int:pk>/', Measur.as_view()),
]
