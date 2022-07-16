from django.shortcuts import render
from django.http import HttpResponse
import json
from CalendaReporter.Models.MCalendar import Calendar
from CalendaReporter.Controllers.CReportController import ReportController

def get(request, name, rangeFrom, rangeTo):
    calendar = Calendar(name)
    report = calendar.reportize(rangeFrom, rangeTo).get()
    ore_lavorate = ReportController.countHours(report, ["Lavoro", "Lavoro #smartworking"])

    return HttpResponse(json.dumps({
        'status': 'success',
        'data': {
            'range': {
                'from': report.rangeFrom,
                'to': report.rangeTo,
            },
            'hours': ore_lavorate,
        }
    }))