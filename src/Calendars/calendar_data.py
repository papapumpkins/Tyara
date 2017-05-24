
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient import sample_tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Tyara Calendar Access'



def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())


def CreateAlarm(Summary,Title,StartTime,RepeatOrNot):
    #Authentication Check!
    main()

    '''Collect Reminder information. 
    1. Start Time (no End time implemented for now. Event will end at 0 mins by default
    2. Title  = Reminder title collected from sin_dialog
    3. Attendees = None
    4. RepeatOrNot = Boolean
    '''
    service = discovery.build('calendar', 'v3')

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    event = {
        'summary': 'Tyara Alarm',
        'location': 'Home',
        'description': 'Morning Alarm.',
        'start': {
            'dateTime': '2015-05-25T07:00:00-07:00',
            'timeZone': 'India/Kolkata',
        },
        'end': {
            'dateTime': '2017-05-25T07:00:00-07:00',
            'timeZone': 'India/Kolkata',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            {'email': 'res.neelotpalnag@gmail.com'},
        ],
        'reminders': {
            'useDefault': False,
        },
    }

    event[0] = Summary
    event[2]= Title
    event[3][1] = StartTime.isoformat()
    event[4][1] = StartTime.isoformat()

    if(RepeatOrNot==1):
        event[6] = ['RRULE:FREQ=DAILY;COUNT=1']
    else: event[6] = ['RRULE:FREQ=ONCE;COUNT=1']

    # now publish the event !
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

def setAlarm(sin_dialog):
    Summary = "Tyara Alarm"
    Title = "Wake Up"
    StartTime = '2017-05-25T17:00:00-07:30'
    RepeatOrNot = 0


if __name__ == '__main__':
    main()

setAlarm("YooHoo")