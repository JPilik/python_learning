import PySimpleGUI as sg
from pythonping import ping
import ipaddress
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
'''A simple program that generates characters for D & D 5E.'''

results = []

    

def main():
    '''main point of execution method in python'''
    menu_def = [['File', 'Exit', ], ['Help', 'About...'], ]
    layout = [
        [sg.Menu(menu_def)], 
        [sg.Text(text="Simple Application to run ping.", font=('Arial Bold', 15), size=20, expand_x=True, justification='center')], 
        [sg.InputText(expand_x=True),sg.Button("Ping")], 
        [sg.Multiline("", key='-IN-', expand_x=True, expand_y=True, size=(None, 20))]]

    # Create the window
    #sg.theme('Dark')
    window = sg.Window("Ping Application", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == 'Ping':
            try:
                ip = str.strip(values[1])
                addy = ipaddress.ip_address(ip)
                
                results = ping(ip)
                
                for result in results:
                    window['-IN-'].update(result)
            except ValueError:
                print(str.strip(values[1]))
            
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()
if __name__ == '__main__':
    main()
