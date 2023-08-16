"""
bill_sender.py:

Modules used:

- database: create_session used to make changes to the database, Bills class needed so it can find the data in the database.
- message_sender: uses twilio function to send message to phone within check_upcoming_bills
- datetime: timedelta used to get a specific day, datetime to get the current dates
"""

from database import create_session, Bills
from message_sender import send_twilio_message
from datetime import datetime, timedelta

# Using the datatime library to get the current dates and times
current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

# Creating a session to add data to the database
session = create_session()


# Function to check upcoming bills in the database where the bill date matches the reminder date
def check_upcoming_bills():
    days_in_advance = 1
    reminder_date = current_date + timedelta(days=days_in_advance)
    reminder_day = reminder_date.day
    reminder_month = reminder_date.month
    reminder_year = reminder_date.year

    reminders = session.query(Bills).filter(
        Bills.Bill_Date == f'{reminder_year}-{reminder_month:02d}-{reminder_day:02d}'
    ).all()

    # If the Bill matches the reminder date, the notification is sent using send_twilio_message
    if reminders:
        for reminder in reminders:
            print('Bill Found!')
            message_body = f'Bill Name: {reminder.Name} | Amount: £{reminder.Amount}'
            send_twilio_message(message_body)

    else:
        print('No Bills due')
