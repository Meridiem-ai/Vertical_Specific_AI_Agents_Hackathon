import os
import logging
from simple_salesforce import Salesforce
from dotenv import load_dotenv
from langchain.agents import tool

# Load environment variables
load_dotenv()

@tool
def add_contact(first_name: str, last_name: str, title: str = "", assistant_name: str = "", 
                assistant_phone: str = "", department: str = "", description: str = "", 
                email: str = "", phone: str = "", other_phone: str = "", 
                birthdate: str = "2000-01-01") -> str:
    """
    Adds a new contact in Salesforce.

    Args:
        first_name (str): First name.
        last_name (str): Last name.
        title (str, optional): Job title. Defaults to "".
        assistant_name (str, optional): Assistant's name. Defaults to "".
        assistant_phone (str, optional): Assistant's phone number. Defaults to "".
        department (str, optional): Department. Defaults to "".
        description (str, optional): Description. Defaults to "".
        email (str, optional): Email address. Defaults to "".
        phone (str, optional): Phone number. Defaults to "".
        other_phone (str, optional): Alternative phone number. Defaults to "".
        birthdate (str, optional): Birthdate in ISO 8601 format. Defaults to "2000-01-01".

    Returns:
        str: Status message of the operation.
    """
    try:
        # Fetch Salesforce access token and instance URL from environment
        access_token = os.getenv('SALESFORCE_ACCESS_TOKEN')
        instance_url = os.getenv('SALESFORCE_INSTANCE_URL')

        if not access_token or not instance_url:
            return "Salesforce access token or instance URL not found. Please check environment variables."

        # Establish Salesforce connection
        sf = Salesforce(instance_url=instance_url, session_id=access_token)

        # Create contact in Salesforce without AccountId
        sf.Contact.create({
            "FirstName": first_name,
            "LastName": last_name,
            "Title": title,
            "AssistantName": assistant_name,
            "AssistantPhone": assistant_phone,
            "Department": department,
            "Description": description,
            "Email": email,
            "Phone": phone,
            "OtherPhone": other_phone,
            "Birthdate": birthdate
        })

        return "The contact has been successfully created"

    except Exception as e:
        logging.error(f"ERROR in function add_contact: {e}")
        return f"ERROR: Could not add contact. Details: {e}"
