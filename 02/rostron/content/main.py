'''A simple program that pings targets.'''
import PySimpleGUI as sg
from event_loop import event_loop
    
def main():
    '''main point of execution method in python'''
    menu_def = [['&File', '&Quit'], ['&Help', 'No Help For You']]
    colorLst = ['Black', 'White', 'Royalblue', 'Green', 'Yellow', 'Purple', 'Red', 'Orange', 'Cyan', 'Olive', 'Pink', 'Chartreuse', 'Slateblue']
    sg.theme(new_theme = 'Topanga')
    movingButton = sg.Button('text', key = '--Moving--')
    multiline = sg.Multiline('', key = '--OUT--', expand_x = True, expand_y = True, size = (80,20), reroute_stdout = True, reroute_stderr = True, reroute_cprint = True, write_only = True)
    layout = [[sg.Menu(menu_def, background_color = 'White', text_color = 'Black')],
              [sg.Text('Test for me daddy', justification = 'center', expand_x = True, expand_y = True, font = ('Arial', 30)), movingButton, sg.Combo(values = colorLst, default_value = 'Black', key = '--DropDown--', readonly = True), sg.Button('Test')],
              [multiline]]
    x,y = 0, 0

    window = sg.Window("Test Application", layout, finalize = True)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel', 'Quit'):
            break
        if event in ('Test'):
            multiline.print('This is a test', text_color = values['--DropDown--'])
        if event in ('No Help For You'):
            window.disappear()
            sg.popup('You Thought')
            window.reappear()
        
    
    window.close()

if __name__ == '__main__':
    main()
