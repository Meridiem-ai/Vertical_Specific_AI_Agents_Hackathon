import sys
import os
import json
import requests
from dotenv import load_dotenv
from langchain.agents import tool

# Load environment variables from a .env file
load_dotenv()

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """
    Sends an email.
    Args:
        to (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The content of the email.
    Returns:
        A message indicating whether the function executed successfully.
    """
    try:
        # Construct the HTML body
        newline = '\n'
        body_html = f"<p>{body.replace(newline, '<br>')}</p>"
        
        # Get the access token from environment variables
        access_token = os.getenv('MICROSOFT_ACCESS_TOKEN')
        if not access_token:
            return "Access token not found in environment variables."

        # Email API endpoint
        EMAIL_ENDPOINT = "https://graph.microsoft.com/v1.0/me/sendMail"
        
        # Email content
        email_msg = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "HTML",
                    "content": body_html
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": to
                        }
                    }
                ]
            },
            "saveToSentItems": "true"
        }

        # Headers for the API request
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        # Send the email
        response = requests.post(EMAIL_ENDPOINT, headers=headers, data=json.dumps(email_msg))
        
        # If unauthorized, access token might need to be refreshed
        if response.status_code == 401:
            return "Unauthorized. Please check the access token."

        # Raise exception if the request failed
        response.raise_for_status()

        return "Email sent successfully!"

    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"



# kwargs = {
#     'to': "mawaf02@gmail.com",
#     'subject': "Test Email",
#     'body': "This is the body of the test email."
# }

# print(send_email(**kwargs))