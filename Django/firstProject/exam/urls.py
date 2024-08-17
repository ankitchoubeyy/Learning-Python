from django.contrib import admin
from django.urls import path
from exam import views

urlpatterns = [
    path('notice', views.notice),
    path('admitcard', views.admitcard),
    path('result', views.result),
]