"""
message_sender.py:

This script sends SMS messages using the Twilio API.

Modules Used:
- os: Allows access to environment variables.
- twilio.rest.Client: Provides functionality to send messages using the Twilio service.

"""
import os
from twilio.rest import Client

# Set Twilio Account SID and Auth Token using environment variables


# Create a Twilio client
client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])


def send_twilio_message(message_body):
    """
    Sends an SMS message using the Twilio API.

    Args:
        message_body (str): The text of the message.

    Returns:
        message: The Twilio message object.
    """
    message = client.messages \
        .create(
            body=message_body,
            from_='+447700137957',  # Twilio phone number
            to='+447533487088'  # Recipient phone number
    )
    return message
