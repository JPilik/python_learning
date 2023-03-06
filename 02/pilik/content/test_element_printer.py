'''Test module for element_printer_test'''
from element_printer import print_w, printerror_w

def test_print_w():
    element = ""
    print_w('test', element)
    print(element)

def test_print_error_w():
    element = ""
    printerror_w('test', element)
    print(element)

