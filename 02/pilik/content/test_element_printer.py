'''Test module for element_printer_test'''
import pytest
from mocks.mock_element import Element
from element_printer import print_w, printerror_w


@pytest.fixture(name="get_element")
def fixture_element():
    '''Fixture to setup an element for Mock Tests'''
    return Element()


def test_print_w(get_element):
    '''Test of the ability to send a message to an element'''
    element = get_element
    print_w('test', element)
    print(element)

def test_print_error_w(get_element):
    '''Test of the ability to send an error message to an element'''
    element = get_element
    printerror_w('test', element)
    print(element)
