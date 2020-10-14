from django.urls import path
from . import views
from spyder import views as spyder_view

urlpatterns = [
    path('submit', views.submit),
    path('random', spyder_view.randomIntPage),
    path('check', spyder_view.submitPage),
    path('<slug:slug>', views.chall)
]
