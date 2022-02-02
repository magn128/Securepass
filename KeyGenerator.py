import rsa
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("Generate key")], [sg.Button("Get key")]]


window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == "Generate key":
        publicKey, privateKey = rsa.newkeys(512)
        print(publicKey,privateKey)
        f1= open("publickey.txt","w+")
        f2= open("privatekey.txt","w+")
        f1.write(str(publicKey))
        f2.write(str(privateKey))
        f1.close()
        f2.close()
    if event == "Get key":
        f1= open("publickey.txt","r+")
        f2= open("privatekey.txt","r+")
        publickey= f1.read()
        privatekey= f2.read()
        print(publicKey)
        print(privateKey)
        f1.close()
        f2.close()
        
