from django.shortcuts import render
from django.http import HttpResponse
from CalendaReporter.Models.MCalendar import Calendar

def get(request, name, rangeFrom, rangeTo):
    calendario = Calendar(name)
    ore_lavorate = calendario.countHoursInRange()
    return HttpResponse('Info calendario ' + calendario.name + ". Hai lavorato " + str(ore_lavorate) + " ore.")