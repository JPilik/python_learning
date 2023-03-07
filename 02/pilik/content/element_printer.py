'''Library uses for printing to an element'''

def print_w(result, element):
    '''Prints a meessage to the element'''
    return print_base(result, 'lime', element)

def printerror_w(result, element):
    '''Prints an error message to the element'''
    return print_base(result, 'red', element)

def print_base(text, color, element):
    '''Prints a message with a specified collor'''
    element.print(text, end = None,
        sep = None,
        text_color = color,
        background_color = 'black',
        justification = None,
        font = None,
        colors = None,
        t = None,
        b = None,
        c = None,
        autoscroll = True)
    return True
