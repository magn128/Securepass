from tkinter import CENTER
import PySimpleGUI as sg
from PIL import Image
import io

sg.ChangeLookAndFeel('darkblue16')


def win1_layout():
    layout = [
        [sg.Frame('',[[sg.Text('SecurePass', size=(120, 1), justification='center'),]])],
        [sg.Frame('',[[sg.Text('media', size=(20,20))]])]
    ]
    return layout

window = sg.Window('SecurePass', win1_layout())


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'exit'):
        break
window.close()