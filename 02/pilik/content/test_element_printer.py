'''Test module for element_printer_test'''
from element_printer import print_w, printerror_w
class Element:
    def print(self, args,
    end = None,
    sep = None,
    text_color = None,
    background_color = None,
    justification = None,
    font = None,
    colors = None,
    t = None,
    b = None,
    c = None,
    autoscroll = True):
        pass

def test_print_w():
    '''Test ability to do a standard print'''
    element = Element()
    result = print_w('test', element)
    assert result == True

def test_print_error_w():
    '''Test ability to do a standard print'''
    element = Element()
    result = printerror_w('test', element)
    assert result == True
