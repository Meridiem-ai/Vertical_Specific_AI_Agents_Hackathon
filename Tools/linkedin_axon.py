import requests
import os
import json
from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()

# person_name = "Cyril Thielemans"

# message = "Hello Cyril this is a test"

@tool
def send_linkedin_msg(person_name: str, message: str) -> int:
    """Sends a message to a person on LinkedIn and returns a status message.

    Args:
        person_name (str): The name of the person to send the message to, written exactly as specified by the user in the query.
        message (str): The content of the message to be sent.

    Returns:
        str: A message indicating whether the message was successfully sent or not.
    """
    # Check if both the person's name and message are provided
    if not person_name or not message:
        return f"Failed to send the message. Missing person name or message."

    url_listconv = "https://svc.sandbox.anon.com/actions/linkedin/listConversations"

    url_sendmsg = "https://svc.sandbox.anon.com/actions/linkedin/sendMessage"

    headers1 = {
        "X-Anon-App-User-Id": os.getenv('X-Anon-App-User-Id'),
        "Authorization": f"Bearer {os.getenv('Anon_API_key')}"
    }

    response1 = requests.request("GET", url_listconv, headers=headers1)
    conversations_link = conversations_link = json.loads(response1.text)

    # Loop through all conversations
    for conversation in conversations_link.get("conversations", []):
        # Loop through all attendees in each conversation
        for attendee in conversation.get("attendees", []):
            # Check if the attendee's name matches the person_name
            if attendee.get("name") == person_name:
                print("\nfound it\n")
                # Return the conversation ID if a match is found
                conversationId = conversation.get("id")

    if not conversationId:
        return "the message was not succesfully send, continue on"


    payload = {
        "message": message,
        "conversationId": conversationId
    }
    headers = {
        "X-Anon-App-User-Id": os.getenv("X-Anon-App-User-Id"),
        "Authorization": f"Bearer {os.getenv('Anon_API_key')}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url_sendmsg, json=payload, headers=headers)
    print("success", json.loads(response.text)["success"])
    if json.loads(response.text)["success"]:
        return "the message was succesfully send"
    else:
        return "the message was not succesfully send, continue on"
    