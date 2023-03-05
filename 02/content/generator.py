import PySimpleGUI as sg
from pythonping import ping
from time import sleep
import ipaddress
'''A simple program that generates characters for D & D 5E.'''

results = []
sg.theme('DarkBlue4')
pingstate = False

def print_w(text, window):
    window['-IN-'].print(text, end = None,
        sep = None,
        text_color = 'lime',
        background_color = 'black',
        justification = None,
        font = None,
        colors = None,
        t = None,
        b = None,
        c = None,
        autoscroll = True)

def printerror_w(text, window):
        window['-IN-'].print(text, end = None,
        sep = None,
        text_color = 'red',
        background_color = 'black',
        justification = None,
        font = None,
        colors = None,
        t = None,
        b = None,
        c = None,
        autoscroll = True)

def send_pings(window, addy):
    for result in ping(addy):
        print_w(result, window)
    

def main():
    global pings
    '''main point of execution method in python'''
    #sg.theme_previewer()
    menu_def = [['File', 'Exit', ], ['Help', 'About...'], ]
    layout = [
        [sg.Text(text="Simple Application to run ping.", font=('Arial Bold', 15), size=20, expand_x=True, justification='center', grab=True), sg.T(sg.SYMBOL_X, enable_events=True, k='Exit')], 
        [sg.InputText(expand_x=True),sg.Button("Ping")], 
        [sg.Multiline("", key='-IN-', expand_x=True, expand_y=True, size=(None, 20), background_color='black',
    text_color = 'lime',)]]

    
    addy = ""
    # Create the window
     
    window = sg.Window("Ping Application", layout, no_titlebar=True)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == 'Ping':
            try:
                ip = ipaddress.ip_address(str.strip(values[1]))
                addy = str.strip(values[1])
                send_pings(window, addy)
            except ValueError:
                printerror_w(f'{str.strip(values[1])} is not a valid IP address.', window)
            
        
        if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
            break

        if event == 'Min':
            print('minimize')

        if event == 'About...':
            window.disappear()
            sg.popup('Pinger', 'Version 1.0', 'PySimpleGUI Version', sg.get_versions())
            window.reappear()

        
    window.close()
if __name__ == '__main__':
    main()
