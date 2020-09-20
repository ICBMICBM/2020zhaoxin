from django.shortcuts import render
from django.http import HttpResponse
from .models import user


def index(request):
    return render(request, 'login.html')

def renderLoginRegister(request):
    return render(request, 'login.html')

def login(request):
    email = request.GET['email']
    password = request.GET['password']
    if user.objects.filter(userEmail=email,userPassword=password).count() == 1:
        request.session['email'] = email
        return HttpResponse("login done")
    else:
        return HttpResponse("login failed")

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

