from CalendaReporter.Models.MReport import Report

class Calendar:
    def __init__(self, name):
        self.name = name

    def reportize(self, rangeFrom, rangeTo):
        return Report(rangeFrom, rangeTo)
        