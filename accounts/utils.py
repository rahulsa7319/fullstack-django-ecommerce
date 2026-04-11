from twilio.rest import Client
from django.conf import settings
import re

def send_welcome_sms(phone_number, username):
    """
    Sends a welcome SMS to the new user using the Twilio API.
    """
    message_text = f"Welcome to Hopping, {username}! Thank you for registering with us."
    
    # Twilio configuration from settings
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_number = settings.TWILIO_PHONE_NUMBER

    if not all([account_sid, auth_token, twilio_number]) or "your_account_sid_here" in account_sid:
        print("Twilio settings are not properly configured in .env file.")
        return False

    try:
        client = Client(account_sid, auth_token)
        
        # 1. Strip ALL non-digit characters to get the raw number
        raw_digits = re.sub(r'\D', '', str(phone_number))
        
        # 2. Handle Indian number logic
        if len(raw_digits) == 10:
            # Standard 10-digit Indian number
            formatted_phone_number = f"+91{raw_digits}"
            print(f"Auto-formatting 10-digit number to India: {formatted_phone_number}")
        elif len(raw_digits) == 12 and raw_digits.startswith('91'):
            # 12-digit number already starting with 91
            formatted_phone_number = f"+{raw_digits}"
        else:
            # Fallback for other international formats
            # Clean but keep the '+' if it was originally there
            formatted_phone_number = re.sub(r'[^\d+]', '', str(phone_number))
            if not formatted_phone_number.startswith('+'):
                formatted_phone_number = f"+{formatted_phone_number}"
        
        message = client.messages.create(
            body=message_text,
            from_=twilio_number,
            to=formatted_phone_number
        )
        
        print(f"SMS successfully sent to {formatted_phone_number}. SID: {message.sid}")
        return True
                
    except Exception as e:
        print(f"Error sending SMS to {phone_number}: {str(e)}")
        # Log Twilio specific error if available
        if hasattr(e, 'code'):
            print(f"Twilio Error Code: {e.code}")
        return False
