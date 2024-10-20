# import os
# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build
# import datetime
# from googleapiclient.errors import HttpError
# from dotenv import load_dotenv
# from langchain.agents import tool
# load_dotenv()

# @tool
# def list_events(maxResults: int = 10) -> str:
#     """Return the last n events from Google Calendar. Use this one by default to find events.

#     Args:
#         maxResults (int, optional): The number of last events to return. Defaults to 10.

#     Returns:
#         str: A string containing the n last events.
#     """
#     try:
#         # Access token is now fetched from environment variables
#         access_token = os.getenv("GOOGLE_CALENDAR_ACCESS_TOKEN")
#         if not access_token:
#             return "Google Calendar access token not found. Make sure it is set in the environment variables."

#         creds = Credentials(token=access_token)

#         try:
#             service = build('calendar', 'v3', credentials=creds)
#             now = datetime.datetime.now().isoformat() + "Z"
#             print('Getting the upcoming events')
#             event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=maxResults, singleEvents=True, orderBy="startTime").execute()
#             events = event_result.get("items", [])

#             if not events:
#                 return "No upcoming events found!"

#             return "\n".join([f'{event["start"].get("dateTime", event["start"].get("date"))} {event["summary"]}' for event in events])
#         except HttpError as error:
#             print("An error occurred: ", error)
#             return "An error occurred while fetching events."
#     except Exception as e:
#         print("An error occurred: ", e)
#         return "An error occurred during authentication."
