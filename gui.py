import tkinter as tk
from tkinter import ttk
from main import create_bills
from bill_sender import check_upcoming_bills
window = tk.Tk()
window.title('Bills Tracker')
window.geometry('600x300')

upcoming_bills = create_bills()

column_names = list(upcoming_bills[0].keys())

column_names[column_names.index("Bill_Date")] = "Bill Date"

tree = ttk.Treeview(window, columns=column_names,show='headings')

for col in column_names:
    tree.heading(col, text=col)

for bill in upcoming_bills:
    formatted = f'£{bill["Amount"]}'
    tree.insert('','end',values=(bill['Name'],formatted, bill['Bill_Date']))

tree.pack()


check_button = ttk.Button(window, text="Check Upcoming Bills", command=check_upcoming_bills)
check_button.pack()

window.mainloop()
