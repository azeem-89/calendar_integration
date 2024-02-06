# mycalendar_app/google_calendar.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def authenticate_user(request):
    credentials = None
    if 'google_auth_token' in request.session:
        credentials = Credentials.from_authorized_user_info(request.session['google_auth_token'])

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'path/to/client_secret.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        request.session['google_auth_token'] = credentials.to_authorized_user_info()
    
    return credentials

def create_event(credentials, event_details):
    service = build('calendar', 'v3', credentials=credentials)

    event = service.events().insert(
        calendarId='primary',
        body=event_details
    ).execute()

    return event['id']
