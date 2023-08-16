from database import Bills, create_session
from datetime import datetime

current_date = datetime.now()
current_month = current_date.month
current_year = current_date.year


def add_bill_to_database(session, name, amount, day):
    bill_date = datetime(current_year, current_month, day).date()
    new_bill = {
        'Name': name,
        'Amount': amount,
        'Bill_Date': bill_date
    }

    bill_record = Bills(**new_bill)
    session.add(bill_record)
    session.commit()
