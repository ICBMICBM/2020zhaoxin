from django.shortcuts import render
from django.http import HttpResponse
from .models import user
import json


def index(request):
    return render(request, 'login.html')

def renderLoginRegister(request):
    return render(request, 'login.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if user.objects.filter(userEmail=email,userPassword=password).count() == 1:
        request.session['email'] = email
        return HttpResponse(json.dumps({"status":"success"}))
    else:
        return HttpResponse(json.dumps({"status":"failed"}))

def register(request):
    username = request.GET['username']
    password = request.GET['password']
    email = request.GET['email']
    qq = request.GET['qq']
    try:
        if user.objects.filter(userName=username).count() == 0:
            user.objects.create(userName=username,userPassword=password,
                                userEmail=email,userQQ=qq)
            return HttpResponse("register done")
    except Exception as e:
        return HttpResponse(e)

