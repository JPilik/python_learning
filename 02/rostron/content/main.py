'''A simple program that pings targets.'''
import PySimpleGUI as sg
from event_loop import event_loop
    
def main():
    '''main point of execution method in python'''
   
    window = sg.Window("Ping Application", [
        [sg.T("Ping Application")]
        ])
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
            break
    window.close()

if __name__ == '__main__':
    main()
