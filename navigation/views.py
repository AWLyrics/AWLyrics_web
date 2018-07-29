from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import generateForm
def index(request):
    return render(request, "index.html", {"info":""})
def generateFun(name):
    name = name +"\r"+ name[::-1]
    name = name + name
    name = name + name
    name = name + name
    name = name + name
    name = name + name
    name = name + name
    return name
def generate(request, name):
    if request.is_ajax():
        response = generateFun(name)
        return HttpResponse(response)
    else :
        return render(request, "index.html", {"info":""})
