import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def main(request):
    context = {'month':datetime.datetime.now().month}
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))

def boardList(request):
    context = {'month':datetime.datetime.now().month}
    template = loader.get_template('board-list.html')
    return HttpResponse(template.render(context, request))
def boardView(request):
    context = {'month':datetime.datetime.now().month}
    template = loader.get_template('board-view.html')
    return HttpResponse(template.render(context, request))