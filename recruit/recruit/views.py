from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import user, signUp
from chall.models import flag
from tools.signUpForm import signUpForm
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
    if user.objects.filter(userEmail=email, userPassword=password).count() == 1:
        request.session['email'] = email
        return HttpResponse(json.dumps({"status": "success"}))
    else:
        return HttpResponse(json.dumps({"status": "failed"}))


def register(request):
    # 暂时使用明文储存密码
    password = request.POST['password']
    email = request.POST['email']
    qq = request.POST['qq']
    try:
        if user.objects.filter(userEmail=email).count() == 0:
            user.objects.create(userPassword=password,
                                userEmail=email, userQQ=qq)
            request.session['email'] = email
            return HttpResponse(json.dumps({"status": "success"}))
        else:
            return HttpResponse(json.dumps({"status": "failed"}))
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "failed", "info": e}))


def gameSignUp(request):
    if request.method == 'POST':
        email = request.session['email']
        u = user.objects.get(userEmail=email)
        flagCount = u.userFlagSum
        solved = u.solved
        password = u.userPassword
        form = signUpForm(request.POST)
        if form.is_valid():
            sid = form.cleaned_data['sid']
            try:
                assert str(sid).startswith('2020') or str(sid).startswith('2019') or str(sid).startswith(
                    '2018') and len(str(sid)) == 12
            except AssertionError:
                error = "喂 你真的知道学号是什么吗"
                return render(request, "error.html", {"error": error})
            name = form.cleaned_data['name']
            qq = form.cleaned_data['QQ']
            if signUp.objects.filter(userEmail=email).count() == 0:
                try:
                    signUp.objects.create(userEmail=email, userPassword=password, userQQ=qq,
                                          userFlagCount=flagCount, solved=solved, sid=sid, name=name)
                    print("sign up success")
                    return HttpResponseRedirect("/user")
                except Exception as e:
                    HttpResponse(e)
            elif signUp.objects.filter(userEmail=email).count() == 1:
                try:
                    signUp.objects.filter(userEmail=email).update(userPassword=password, userQQ=qq,
                                                                  userFlagCount=flagCount, solved=solved, sid=sid,
                                                                  name=name)
                except Exception as e:
                    HttpResponse(e)
                return HttpResponseRedirect("/user")
            else:
                error = "???"
                return render(request, "error.html", {"error": error})
        else:
            return HttpResponseRedirect("/user")
    else:
        form = signUpForm()
        return render(request, "signup.html", {'form': form})


def logout(request):
    request.session['email'] = None
    return HttpResponseRedirect("/index")


def me(request):
    if request.session['email']:
        if signUp.objects.filter(userEmail=request.session['email']).count() == 1:
            signedUser = signUp.objects.get(userEmail=request.session['email'])
            name = signedUser.name
            sid = signedUser.sid
            qq = signedUser.userQQ
            signed = "你已报名招新赛"
        else:
            signed = "你还没有报名招新赛"
            name = ""
            sid = ""
            qq = ""

        email = request.session['email']
        u = user.objects.get(userEmail=email)
        solved = json.loads(u.solved).keys()
        flags = flag.objects.all().count()
        progress = len(solved) / flags if len(solved) > 0 else 0
        return render(request, "me.html",
                      {"progress": progress * 100, "signed": signed, "name": name, "sid": sid, "qq": qq})
    else:
        return HttpResponseRedirect("/index")
