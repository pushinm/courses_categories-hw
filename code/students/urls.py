from django.urls import path
from .views import students_view


urlpatterns = [
    path('', students_view, name='students_view'),
    path('<int:pk>/', students_view, name='students_view'),
]