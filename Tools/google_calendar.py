import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()

@tool
def users_free_time(start_date: str = None, end_date: str = None, maxResults: int = 10) -> str:
    """Return events from Google Calendar between specified dates.

    Args:
        start_date (str, optional): The start date in 'YYYY-MM-DD' format. Defaults to None (current date).
        end_date (str, optional): The end date in 'YYYY-MM-DD' format. Defaults to None (no end date).
        maxResults (int, optional): The maximum number of events to return. Defaults to 10.

    Returns:
        str: A string containing the events in the specified date range.
    """
    try:
        # Access token is now fetched from environment variables
        access_token = os.getenv("GOOGLE_CALENDAR_ACCESS_TOKEN")
        if not access_token:
            return "Google Calendar access token not found. Make sure it is set in the environment variables."

        creds = Credentials(token=access_token)

        try:
            service = build('calendar', 'v3', credentials=creds)
            
            # Set timeMin and timeMax
            if start_date:
                # Parse start_date string into datetime object
                time_min = datetime.datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
            else:
                # Default to current time
                time_min = datetime.datetime.utcnow().isoformat() + 'Z'
                
            if end_date:
                # Parse end_date string into datetime object
                # Add one day to include the end_date in the results
                time_max_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                time_max = time_max_date.isoformat() + 'Z'
            else:
                time_max = None  # No upper limit

            # Build the event list request
            events_result = service.events().list(
                calendarId='primary',
                timeMin=time_min,
                timeMax=time_max,
                maxResults=maxResults,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            events = events_result.get('items', [])

            if not events:
                return "No events found in the specified date range."

            # Build the event list string
            event_list = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                summary = event.get('summary', 'No Title')
                event_list.append(f"{start} - {summary}")

            return "\n".join(event_list)
        except HttpError as error:
            print("An error occurred: ", error)
            return "An error occurred while fetching events."
    except Exception as e:
        print("An error occurred: ", e)
        return "An error occurred during authentication."
    
    {"refresh_token": "1//05SEz9UfisDPbCgYIARAAGAUSNwF-L9IrNb0ohT-XHroiYUFBVgmuQ-3njE8qtj5_4R3McG9v_rHwzmPYF9NfD8QGYGAVIoEQwpo"}
