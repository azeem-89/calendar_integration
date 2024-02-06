# my_calendar
 
MyCalendar Project is a Django web application that integrates with Google Calendar API to provide calendar functionality.

## Features
- Authentication with Google Calendar API.
- Display user's calendar events.
- Add, edit, and delete events.
## Installation
 - Clone the repository:

## Prerequisites
- Python and Django installed on your system.
- A Google Cloud Platform (GCP) project with the Calendar API enabled.
- OAuth 2.0 credentials for your GCP project.

## Configuration
- Set up a GCP project and enable the Google Calendar API.
- Create OAuth 2.0 credentials for your project and download the JSON file.
- Place the downloaded JSON file in the calendar prroject directory.

##  Additional Notes
- Make sure to handle error cases such as invalid credentials or unauthorized access gracefully.
- You can customize the appearance and functionality of the calendar display in the home.html template located in the mycalendar_app/templates/ directory.
