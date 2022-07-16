from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Report:
    def __init__(self, rangeFrom, rangeTo):
        self.rangeFrom = rangeFrom
        self.rangeTo = rangeTo

    def get(self):
        # si interfaccia con l'api di gcalendar per tirarsi giù le informazioni
        # e.g. https://github.com/googleworkspace/python-samples/blob/master/calendar/quickstart/quickstart.py
        pass