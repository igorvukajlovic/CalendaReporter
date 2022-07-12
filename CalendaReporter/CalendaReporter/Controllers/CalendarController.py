from django.shortcuts import render
from django.http import HttpResponse

def get(request, name):
    return HttpResponse('Info calendario ' + name)