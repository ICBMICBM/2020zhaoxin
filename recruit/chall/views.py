from django.shortcuts import render
from django.http import HttpResponse
from tools.submitFlagForm import flagForm


def index(request):
    return HttpResponse("index")

def submit(request):
    if request.method == 'POST':
        form = flagForm(request.POST)
        if form.is_valid():
            flag = form.cleaned_data['flag']
        return HttpResponse(flag)
    else:
        form = flagForm()
        return render(request,"submit.html",{'form':form})

# Create your views here.
