from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import generateForm
def index(request):
    if request.method == "POST":
        form = generateForm(request.POST)
        if form.is_valid():
            return  render(request, "index.html",{"info":request.POST['name']})
        else :
            return  render(request, "index.html",{"info":"not valid"})
    elif request.is_ajax():
        return HttpResponse("111")
     
    else :
        return render(request, "index.html", {"info":""})
def generateFun(name):
    name = name + name[::-1]
    return name
def generate(request, name):
    if request.is_ajax():
        response = generateFun(name)
        return HttpResponse(response)
    else :
        return render(request, "index.html", {"info":""})
