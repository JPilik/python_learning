'''Code that represents the event loop of the gui'''

from pings import send_pings


def event_loop(sg, window):
    '''Event Loop of the pysimplegui application'''
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == 'Ping':
            send_pings(window['-IN-'], values[1])
        
        if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
            break

        if event == 'About...':
            window.disappear()
            sg.popup('Pinger', 'Version 1.0', 'PySimpleGUI Version', sg.get_versions())
            window.reappear()
    window.close()