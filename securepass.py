import PySimpleGUI as sg
from PIL import Image
import io

sg.ChangeLookAndFeel('darkblue16
')


def win1_layout():
    layout = [[ sg.Text('SecurePass'), sg.Text(size=(15, 1))]
            ]
    return layout

window = sg.Window('SecurePass', win1_layout())

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'exit'):
        break
window.close()