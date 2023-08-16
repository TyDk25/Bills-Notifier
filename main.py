"""
Automated Bill Sender
Automates managing and tracking of upcoming bills

libraries Used:
- datetime: For working with dates and times
- schedule: For scheduling tasks at specific intervals
- time: Allows the while loop to delay
- database: Contains functions for setting up the database and creating sessions
- bill_sender: Contains 'check_upcoming_bills' function to send reminders

"""

from datetime import datetime
import schedule
import time
from database import setup_database, create_session, Bills
from bill_sender import check_upcoming_bills
from add_new_bill import add_bill_to_database

# Using the datetime library to get the current date
current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

setup_database()
session = create_session()


def create_bills():
    # Creating a dictionary of Bills, the day they come out and their amounts
    bill_data = {
        'Names': ['Car Insurance', 'Phone', 'Flex', 'Spotify', 'The Gym', 'Road Tax', 'YouTube', 'AppleCare', 'Voxi'],
        'Days': [17, 25, 25, 26, 2, 2, 3, 8, 11],
        'Amounts': [216, 35, 5, 3, 25, 19, 7, 12.50, 12]
    }

    # Using a for loop to zip the dictionary together
    upcoming_bills = []
    for name, amount, days in zip(bill_data["Names"], bill_data["Amounts"], bill_data["Days"]):
        bill = {
            'Name': name,
            'Amount': amount,
            'Bill_Date': datetime(current_year, current_month, days).date(),
        }
        upcoming_bills.append(bill)

    # Add bills to the database
    for bill in upcoming_bills:
        bill_record = Bills(**bill)
        session.add(bill_record)

    # Commit changes to the database
    session.commit()

    return upcoming_bills


create_bills()



def prompt_new_bill():

    answer = input("Do you want to add a new bill? (yes/no): ")
    if answer.lower() == "yes":
        name = input("Enter bill name: ")
        amount = float(input("Enter Bill Amount: "))
        day = int(input("Enter bill due day: "))
        add_bill_to_database(session, name, amount, day)




# Schedule the check_upcoming_bills function
schedule.every(10).seconds.do(check_upcoming_bills)

if __name__ == '__main__':
    prompt_new_bill()
    # Run the scheduling loop
    while True:
        schedule.run_pending()
        time.sleep(1)
