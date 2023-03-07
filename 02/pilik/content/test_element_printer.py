'''Test module for element_printer_test'''
from element_printer import print_w, printerror_w
from mocks.mock_element import Element

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
