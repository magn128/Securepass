from pdb import run
import PySimpleGUI as sg
import os
import sys
import ctypes
import random
from sqlite import createloginTable, insert, createcategoryTable
import sqlite3




def test_func():
    global create
    create = 'veryglobal'
    print (create)
    
class key_gen_1:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        for root, directories, files in os.walk(os.path.join(self.path, 'jesus')):
            self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'jesus.jpg'))

sg.theme('BluePurple')
# Main - hovedside
def main():
    main = [
        #row01
        [sg.Frame('',[[sg.Text('Securepass', justification='center', size=(87, 1), font=(15))]])],
        #row02
        [sg.Frame('',[[sg.Text('Categories', justification='center', size=(20, 20))]]),
        sg.Frame('',[[sg.Text('Login info', size=(96, 20))]])],
        [sg.Button('Create Category'),
        sg.Button('Add login')]
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
        [sg.Text('Name:', size=(15, 1)), sg.InputText('', key='DB-name')],
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





application = key_gen_1()
window = sg.Window('SecurePass', start())

def login_func():
    global window, window2, window3
    run_create_win = False
    run_main_win = False
    while True:
        event, values = window.read()
        print(event, values)
        if event in ('Login'):

            window.Hide()
            conn = sqlite3.connect(values['Database_name'])
            # Cursor to execute commands
            c = conn.cursor()
            #conn.commit()

            window3 = sg.Window('SecurePass', main())
            run_main_win = True
            break

        if run_main_win:
            main_func()

        
        if event == 'Create database':
            window.Hide()
            window2 = sg.Window('SecurePass', create())
            run_create_win = True
            break

        
    
    if run_create_win:
        create_func()

def create_func():
    global window2, window3
    while True:
        event2, values2 = window2.read()
        print(event2, values2)
        if event2 in (None, 'exit'):
            break
        
        if event2 == 'Create database':
            conn = sqlite3.connect(values2['DB-name'])
            # Cursor to execute commands
            c = conn.cursor()
            
            c.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL
                );''')
            



            conn.commit()
            conn.close()
            print('db made')
            break
    window.UnHide()
    main_func()


def main_func():
    global window3
    while True:
        event3, values3 = window3.read()
        if event3 in (None, 'exit'):
            break
        if event3 == 'add_login':
            
            
            break







login_func()
main_func()


window.close()

