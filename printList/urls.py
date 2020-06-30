from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('printCheck/', views.printCheck.as_view(), name='printCheck'),
    path('printUpload/', views.printUpload, name='printUpload'),
    path('employeeIndex/', views.employeeIndex.as_view(), name='employeeIndex'),
    path('employeeIntake/', views.employeeIntake, name='employeeIntake'),
    path('employeeUpdate/<int:pk>', views.employeeUpdate, name='employeeUpdate'),
    path('employeeMarkPrinted/<int:pk>', views.employeeMarkPrinted, name='employeeMarkPrinted'),
    path('employeeVerifyIndex', views.employeeVerifyIndex.as_view(), name='employeeVerifyIndex'),
    path('employeeDownload/<int:pk>', views.employeeDownload, name='employeeDownload'),
    path('dataExport', views.dataExport, name='dataExport')
]