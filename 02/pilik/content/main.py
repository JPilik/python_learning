'''A simple program that pings targets.'''
import PySimpleGUI as sg
from time import sleep
from event_loop import event_loop

def main():
    '''main point of execution method in python'''
    menu_def = [['File', 'Exit', ], ['Help', 'About...']]
    
    layout = [
        [sg.Menu(menu_def)],
        [sg.Text(text="Simple Application to run ping.", font=('Arial Bold', 15), size=20, expand_x=True, justification='center', grab=True)], 
        [sg.InputText(expand_x=True),sg.Button("Ping")], 
        [sg.Multiline("", key='-IN-', expand_x=True, expand_y=True, size=(None, 20), background_color='black',
    text_color = 'lime')]]
    
    # Create the window
    window = sg.Window("Ping Application", layout)
    event_loop(sg, window)

if __name__ == '__main__':
    main()
