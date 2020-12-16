from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from tools.submitFlagForm import flagForm
from chall.models import flag as dbflag
from recruit.models import user
from json import dumps,loads


def submit(request):
    if request.method == 'POST':
        form = flagForm(request.POST)
        submitted = False
        if form.is_valid():
            chall = form.cleaned_data['chall']
            flag = form.cleaned_data['flag']
            useremail = request.session['email']
            if dbflag.objects.filter(flag=flag,chall=chall).count() == 1:
                try:
                    u = user.objects.get(userEmail=useremail)
                    print(u)
                    s = loads(u.solved)
                    print(s.keys)
                    if str(chall) not in s.keys():
                        u.userFlagSum += 1
                        u.userLatestFlag = flag
                        s[chall] = True
                        u.solved = dumps(s)
                        u.save()
                        submitted = True
                    else:
                        res = '不要重复提交flag'
                        return render(request,"result.html",{"result":res})
                except Exception as e:
                    return HttpResponse(e)
            else:
                submitted = False
        else:
            submitted = False
        yes = ['flag 正确']
        no = ['flag 错误']
        res = yes[0] if submitted is True else no[0]
        return render(request,"result.html",{"result":res})
    else:
        form = flagForm()
        return render(request,"submit.html",{'form':form})

def chall(request,slug):
    # print(slug)
    banned = ['.','/']
    for i in banned:
        if i in slug:
            print('illeagle')
            return HttpResponseRedirect('/index')
    try:
        return render(request,str('chall/' + slug + '.html'))
    except Exception as e:
        print('exception ' + str(e))
        print('not found')
        return HttpResponseRedirect('/index')


