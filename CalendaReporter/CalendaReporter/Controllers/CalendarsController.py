from django.shortcuts import render
from django.http import HttpResponse

def get(request):
    return HttpResponse('Lista dei calendari')