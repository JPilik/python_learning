'''Code that represents the event loop of the gui'''
from pings import send_pings

def event_loop(s_g, window):
    '''Event Loop of the pysimplegui application'''
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == 'Ping':
            send_pings(window['-IN-'], values[1])
            if(values[0] == 'Test' and values[1] == ''):
                break

        if event in (s_g.WIN_CLOSED, 'Cancel', 'Exit'):
            break

        if event == 'About...':
            window.disappear()
            s_g.popup('Pinger', 'Version 1.0', 'PySimpleGUI Version', s_g.get_versions())
            window.reappear()
            if(values[0] == 'Test' and values[1] == ''):
                break
    return window.close()
