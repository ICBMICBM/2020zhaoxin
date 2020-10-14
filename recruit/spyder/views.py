from django.shortcuts import render
from random import randint
from .models import log
from time import time


def randomIntPage(request):
    mat = []
    sum = 0
    for i in range(randint(0,100)):
        rand = randint(0,9999)
        sum += rand
        mat.append(rand)
    logid = log.objects.create(answer=sum).id
    return render(request,"randomIntPage.html",{"ints":mat,"id":logid})


def submitPage(request):
    try:
        id = request.GET['id']
        answer = request.GET['answer']
        getLog = log.objects.get(id=id)
        # print(type(answer),type(getLog.answer))
        if getLog.answer == int(answer) and id and answer:
            if time() - getLog.created.timestamp() < 10:
                res = "chall: flag:" + str(getLog.flag) + "next: /chall/re2"
                timeused = time() - getLog.created.timestamp()
            else:
                res = "too slow"
                timeused = time() - getLog.created.timestamp()
        else:
            res = "no flag for u"
            timeused = time() - getLog.created.timestamp()
    except:
        res = "no flag fro u"
        timeused = 0
    return render(request,"randomSubmit.html",{"res":res,"timeused":timeused})
