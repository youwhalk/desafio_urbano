from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from app import views
from app.views import home, index, readfile, tela3

urlpatterns = [
    path("", views.home, name="home"),
    path("tela2.html", views.index),
    path("tela3.html", views.readfile),
    path('', views.index),
]

