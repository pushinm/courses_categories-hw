from django.urls import path
from .views import show_mainpage
app_name='mainpage'

urlpatterns = [
    path('', show_mainpage, name='mainpage'),
]