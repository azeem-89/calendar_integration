# mycalendar_app/views.py
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialToken
from .google_calendar import authenticate_user, create_event

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    credentials = authenticate_user(request)
    if credentials:
        return redirect('create_event')
    else:
        return render(request, 'login.html')

def logout(request):
    # Add logic to handle logout and redirect to home
    return render(request, 'logout.html')

def create_event_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    credentials = authenticate_user(request)
    event_details = {
        'summary': 'Sample Event',
        'description': 'A sample event created using Django and Google Calendar API',
        'start': {'dateTime': '2024-02-02T10:00:00', 'timeZone': 'UTC'},
        'end': {'dateTime': '2024-02-02T12:00:00', 'timeZone': 'UTC'},
    }

    event_id = create_event(credentials, event_details)
    return render(request, 'event_created.html', {'event_id': event_id})
