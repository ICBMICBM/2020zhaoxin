from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("chall_0 index")

# Create your views here.
