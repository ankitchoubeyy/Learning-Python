from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('greeeting', views.greeting),
    path('about', views.about),
    path('contact', views.contact),
]
