import pyautogui
import PySimpleGUI as sg
import keyboard
import time
import random

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

clicker = ['Single', 'Double']
typer = ['Random', 'Set']
layout = [  [sg.Text('Autoclicker')],
            [sg.Text('Hold "\\" to stop')],
            [sg.Text('Enter speed (ms)'), sg.InputText(), sg.OptionMenu(clicker, default_value='Single', key='clicker'), sg.OptionMenu(typer, default_value='Set', key='typer')],
            [sg.Button('Ok'), sg.Button('Cancel')],
        ]

# Create the Window
window = sg.Window('Autoclicker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    print(values['clicker'])

    try:
        speed = int(values[0]) / 1000
        if speed == 0:
            speed = 100
        print('You entered ', speed)

        #The autoclicking part
        while not keyboard.is_pressed('\\'):
            if (values['clicker'] == 'Single'):
                pyautogui.click()
            else:
                pyautogui.click()
                time.sleep(0.01)
                pyautogui.click()
            
            if (values['typer'] == 'Set'):
                time.sleep(speed)  
            else:
                time.sleep(random.uniform(0.01, speed))
        sg.popup('Stopped!')
    except ValueError:
        sg.popup('Not a Number!')
    


window.close()