from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index),
    path('submit',views.submit),
    path('<slug:slug>',views.chall)
]