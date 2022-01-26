import PySimpleGUI as sg

sg.theme('BluePurple')
# Main - hovedside
def main():
    main = [
        #row01
        [sg.Frame('',[[sg.Text('Securepass', justification='center', size=(84, 1), font=(15))]])],
        #row02
        [sg.Frame('',[[sg.Text('Categories', justification='center', size=(20, 20))]]),
        sg.Frame('',[[sg.Text('Login info', size=(96, 20))]])
        ]
    ]
    return main
# Start - startside
def start():
    start = [
        #row01
        [sg.Text('Database name', size=(15, 1)), sg.InputText('')],
        #row02
        [sg.Text('Password', size=(15, 1)), sg.InputText('', key='Password', password_char='*')],
        #row03
        [sg.Button('Login'),
        sg.Button('Create database')]
    ]
    return start


# Create - lag ny database

def create():
    create = [
        #row01
        [sg.Text('Name:', size=(15, 1)), sg.InputText('')],
        #row02
        [sg.Text('Password', size=(15, 1)), sg.InputText('', key='Password', password_char='*')],
        #row03
        [sg.Button('Create database')]
            ]
    return create


# Add - add ny kategori

def add():
    add = [
        #row01
        [sg.Text('Add Categories', size=(15, 1))],
        #row02
        [sg.Text('Name:', size=(15, 1)), sg.InputText('')],
        #row03 
        [sg.Button('Add')]
        ]
    return add


window = sg.Window('SecurePass', start())


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'exit'):
        break
    if event == 'Create database':
        window.close()
        window2 = sg.Window('SecurePass', create())
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, 'exit'):
                break


window.close()