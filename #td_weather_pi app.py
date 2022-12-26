# -*- coding: utf-8 -*-
# td_weather_pi app
# 12/24/2022
# Last update: 12/24/2022

# notes for tables; need tablulate module; pip install tabulate

# from sense_hat import SenseHat
from tkinter import *
from tkinter import ttk
import pandas as pd
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tabulate import tabulate
import matplotlib.pyplot as plt

#Creation of main GUI and specifications
main = Tk()
main.title("Weather PI")
main.geometry("1600x800")

#Ceation of form layout with grid format
frm = ttk.Frame(main, padding=10)
frm.grid()

#Creatiion of column labels for Data
ttk.Label(frm, text="Temperature", font=("courier", 30, [
          'bold', 'underline'])).grid(row=0, column=0, padx=75, pady=10)
ttk.Label(frm, text="Humiditiy", font=("courier", 30, [
          'bold', 'underline'])).grid(row=0, column=1, padx=300, pady=10)
ttk.Label(frm, text="Pressure", font=("courier", 30, ['bold', 'underline'])).grid(
    row=0, column=2, padx=150, pady=10)


#################################################################
# sense = SenseHat()
# sense.clear()


# while True:
#   temp= sense.get_temperature()
#   print(temp)
#   time.sleep(5)

##############################################################

#Local variables to hold data in labels
temp_val, humi_val, press_val = 0, 0, 0

#Timer function to update data labels
def label_timer():

    #Global variables to hold data in labels
    global temp_val, press_val, humi_val

    temp_val += 1
    press_val += 1
    humi_val += 1
    
    #Updates labels with data in miliseconds
    main.after(1000, label_timer)
    
    
    #Label to hold data values
    ttk.Label(frm, text=temp_val, font=(
        "courier", 40, 'bold')).grid(row=1, column=0, padx=25)
    ttk.Label(frm, text=humi_val, font=("courier", 40, 'bold')
              ).grid(row=1, column=1, padx=25)
    ttk.Label(frm, text=press_val, font=("courier", 40, 'bold')
              ).grid(row=1, column=2, padx=25)

label_timer()

#Creration of quit button
ttk.Button(frm, text="Quit", width=25, command=lambda: [
           os._exit(0)]).grid(column=2, row=4, pady=500)


#High and low tables for temp, humidity, and pressure
table = [['Low', 'High'],
         ['-16', '98']]

#Creation of labels to hold data tables
ttk.Label(frm, text=tabulate(table), font=("courier", 20, 'bold')
          ).grid(row=3, column=0, padx=25, pady=25)
ttk.Label(frm, text=tabulate(table), font=("courier", 20, 'bold')
          ).grid(row=3, column=1, padx=25, pady=25)
ttk.Label(frm, text=tabulate(table), font=("courier", 20, 'bold')
          ).grid(row=3, column=2, padx=25, pady=25)

#List for the temp, humidity, and pressure values
cumu_temp_values = [1, 6]
temp_data_points = {'Cumulative Temperature': cumu_temp_values}

cumu_humi_values = [1, 6]
humi_data_points = {'Cumulative Humidity': cumu_humi_values}

cumu_press_values = [1, 6]
press_data_points = {'Cumulative Pressure': cumu_press_values}

#Timer function to increment list with updated data fro graphs
def graph_timer():

    #Temperature
    cumu_temp_values.append(-2)
    temp_data = pd.DataFrame(temp_data_points)
    figure1 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    temp_canvas = FigureCanvasTkAgg(figure1, master=main)
    temp_canvas.get_tk_widget().place(relx=.01, rely=.300,)
    temp_data = temp_data[['Cumulative Temperature']]
    temp_data.plot(kind='line', ax=ax1, title="Cumulative Temperature")
    
    
    # Humidity 
    cumu_humi_values.append(-3)
    humi_data = pd.DataFrame(humi_data_points)
    figure2 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax1 = figure2.add_subplot(111)
    humi_canvas = FigureCanvasTkAgg(figure2, master=main)
    humi_canvas.get_tk_widget().place(relx=.350, rely=.300,)
    humi_data = humi_data[['Cumulative Humidity']]
    humi_data.plot(kind='line', ax=ax1, title="Cumulative Humidity")
    
    #Pressure
    cumu_press_values.append(-4)
    press_data = pd.DataFrame(press_data_points)
    figure3 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax1 = figure3.add_subplot(111)
    press_canvas = FigureCanvasTkAgg(figure3, master=main)
    press_canvas.get_tk_widget().place(relx=.700, rely=.300,)
    press_data = press_data[['Cumulative Pressure']]
    press_data.plot(kind='line', ax=ax1, title="Cumulative Pressure")

    #Updates data in graps in miliseconds
    main.after(1000, graph_timer)
    temp_canvas.draw()
    humi_canvas.draw()
    press_canvas.draw()

graph_timer()


#Displays main GUI
main.mainloop()
