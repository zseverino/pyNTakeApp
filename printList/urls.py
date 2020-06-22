from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('printCheck/', views.printCheck, name='printCheck'),
    path('printUpload/', views.printUpload, name='printUpload'),
    path('printPrices/', views.printPrices, name='printPrices'),
    path('employeeIndex/', views.employeeIndex.as_view(), name='employeeIndex'),
    path('employeeIntake/', views.employeeIntake, name='employeeIntake')
]