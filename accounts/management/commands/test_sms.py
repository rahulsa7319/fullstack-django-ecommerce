from django.core.management.base import BaseCommand
from accounts.utils import send_welcome_sms

class Command(BaseCommand):
    help = 'Test the Twilio SMS integration'

    def add_arguments(self, parser):
        parser.add_argument('phone_number', type=str, help='The phone number to send the SMS to (in E.164 format, e.g. +1234567890)')
        parser.add_argument('username', type=str, help='The username to include in the welcome message')

    def handle(self, *args, **options):
        phone_number = options['phone_number']
        username = options['username']
        
        self.stdout.write(f'Attempting to send a welcome SMS to {phone_number} for user {username}...')
        
        success = send_welcome_sms(phone_number, username)
        
        if success:
            self.stdout.write(self.style.SUCCESS(f'Successfully sent SMS to {phone_number}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to send SMS to {phone_number}. Check your Twilio settings in the .env file.'))
