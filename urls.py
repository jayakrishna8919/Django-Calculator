from django.urls import path
from calculatorapp import views

urlpatterns = [
    path('main/',views.main,name='main'),
    path('calculate/',views.calculate,name='calculate')
]
