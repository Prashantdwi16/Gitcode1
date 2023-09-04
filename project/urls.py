from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('EmailLoginapi', views.EmailLoginapi),
    path('Signupapi', views.Signupapi),
    path('FileUpload', views.FileUpload),
    path('AllList', views.AllList),
]