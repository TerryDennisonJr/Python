# -*- coding: utf-8 -*-
"""
Coding Challenge Tracker
Terry Dennison

This program takes: 

1. Reads in csv file that contains
    -Coding Challenge
    -Coding Language
    -Entry Date
2. Gather data from csv and transforms into pie graph
3. Takes in user new entries and immediately updates csv/pie graph


Steps:
    1. Line 77, Enter file path of csv file
    2. Line 103, Enter file path of csv file
-Future Updates-
Display the data in table form

"""

from tkinter import *
import tkinter
import os
import csv
from tkinter import ttk
from tkcalendar import Calendar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()

# Creation of root GUI and Title Name
root.geometry("1400x600")
root.title("Coding Progress Logger")

# Label for 'Enter Coding Challenge'
ttk.Label(root, text='Enter Coding Challenge', font=(
    'Sans Serif', 23, 'italic bold')).grid(column=1, row=1)

# Entry Box for entering name of coding challenge
ttk.Label(root, text="Coding Challenge").grid(column=0, row=2)
enter = tkinter.StringVar()
ttk.Entry(root, text="", textvariable=enter).grid(column=1, row=2)

# Dropdown Menu for selecting coding language used for coding challenge
ttk.Label(root, text="Coding Language").grid(column=0, row=3)
cmbx = tkinter.StringVar()
ttk.Combobox(root, values=['Java', 'Python', 'Javascript', ], textvariable=cmbx).grid(
    column=1, row=3)


ttk.Label(root, text="").grid(column=0, row=4)
ttk.Label(root, text="").grid(column=0, row=5)

# Label for completion date of coding challenge
ttk.Label(root, text="Date Completed").grid(column=0, row=6)
cal_items = tkinter.StringVar()

# Calendar for selecing completion date of coding challenge
cal = Calendar(root, foreground='black', selectmode='day',
               textvariable=cal_items,).grid(column=1, row=7)
ttk.Label(root, text="").grid(column=0, row=8)

# Function to read csv, collect count, and put values in a list 
def build_pie_from_list():
    python_counter = 0
    java_counter = 0
    javascript_counter = 0

    global csv_data


# Count totals for challenges in coding languages csv file: 'Python', 'Java' and 'Javascript'
    with open('Enter File Path') as reader_doc:
        doc_reader = csv.reader(reader_doc)
        for row in doc_reader:
            # Determine the count for each coding languages completed
            if(row[1] == ('Python')):
                python_counter += 1
            elif(row[1] == ('Java')):
                java_counter += 1
            elif(row[1] == ('Javascript')):
                javascript_counter += 1
            else:
                continue

    # Put data in List to be used in pie graph
    data_pie = [python_counter, java_counter, javascript_counter]
    csv_data = data_pie


# Call function
build_pie_from_list()

# Function adds user entry (challenge,language,date) into csv file


def add_items_to_csv():
    # Appends new data to file
    with open('Enter File Path', 'a') as challenges:

        # use writer variable to put data entry into csv file
        writer = csv.writer(challenges)
        writer.writerow([enter.get(), cmbx.get(), cal_items.get()])


# Label for 'List/Data'
ttk.Label(root, text='List/Data', font=(
    'Sans Serif', 23, 'italic bold')).grid(column=3, row=1, padx=(400))


# Create/Display Pie Graph Data
def create_pie():

    fig = Figure(figsize=(6, 5), dpi=100, facecolor=('lightsteelblue'))
    ax1 = fig.add_subplot(111)

    code_dict = {'Python': str(csv_data[0]), 'Java': str(
        csv_data[1]), 'Javascript': str(csv_data[2])}

    ax1.pie(csv_data, labels=code_dict.items(), autopct='%1.1f%%')
    canvas = FigureCanvasTkAgg(fig, master=root)

    canvas.get_tk_widget().place(relx=.55, rely=.1,)


# Displays initial values in CSV file in GUI
create_pie()

# Creation of buttons for 'Display Logs', 'Add Entry' and 'Exit'
ttk.Button(root, text="Display Logs").grid(column=0, row=9, pady=100)

ttk.Button(root, text="Add Entry", command=lambda: [
    add_items_to_csv(), build_pie_from_list(), create_pie()]).grid(column=1, row=9)

ttk.Button(root, text="Exit", command=lambda: [
           os._exit(0)]).grid(column=2, row=9)


# display GUI and all embedded components
root.mainloop()
