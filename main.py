from pdb import run
import PySimpleGUI as sg



def test_func():
    global create
    create = 'veryglobal'
    print (create)

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
        [sg.Text('Database name', size=(15, 1)), sg.InputText('', key='Database_name')],
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
    print(create)
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


username = 'magne'
password = '123'

window = sg.Window('SecurePass', start())

def login_func():
    global window, window2, window3, username, password
    run_create_win = False
    run_main_win = False
    while True:
        event, values = window.read()
        print(event, values)
        if event in ('Login'):
            if values['Database_name'] == username and values['Password'] == password:
                window.close()
                window3 = sg.Window('SecurePass', main())
                run_main_win = True
                break

        if run_main_win:
            main_func()

        
        if event == 'Create database':
            window.close()
            window2 = sg.Window('SecurePass', create())
            run_create_win = True
            break
    
    if run_create_win:
        create_func()

def create_func():
    global window2
    while True:
        event2, values2 = window2.read()
        print(event2, values2)
        if event2 in (None, 'exit'):
            break


def main_func():
    global window3
    while True:
        event3, values3 = window3.read()
        if event3 in (None, 'exit'):
            break






login_func()
main_func()


window.close()

