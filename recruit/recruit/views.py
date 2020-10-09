from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import user
import json


def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if user.objects.filter(userEmail=email,userPassword=password).count() == 1:
        request.session['email'] = email
        return HttpResponse(json.dumps({"status":"success"}))
    else:
        return HttpResponse(json.dumps({"status":"failed"}))

def register(request):
    # 暂时使用明文储存密码
    password = request.POST['password']
    email = request.POST['email']
    qq = request.POST['qq']
    try:
        if user.objects.filter(userEmail=email).count() == 0:
            user.objects.create(userPassword=password,
                                userEmail=email,userQQ=qq)
            request.session['email'] = email
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status":"failed","info":e}))

def logout(request):
    request.session['email'] = None
    return HttpResponseRedirect("/index")
