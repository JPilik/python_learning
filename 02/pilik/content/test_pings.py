'''Test module for element_printer_test'''
import pytest
from pings import send_pings
from mocks.mock_element import Element

@pytest.fixture(name="get_element")
def fixture_element():
    '''Method to setup a mock element for testing purposes'''
    return Element()

def raise_(ex):
    '''Method used to raise an exception to ensure we cover that endpoint'''
    raise ex

def test_ping(monkeypatch, get_element):
    '''test of the ping function'''
    monkeypatch.setattr('pings.ping', lambda x: ['line to print'])
    monkeypatch.setattr('pings.ip_address', lambda x: '1.2.3.4')
    element = get_element
    value = 'Success'
    result = send_pings(element, value)
    assert result is True

def test_ping_exception(monkeypatch, get_element):
    '''Method used to test ensure ping throws an exception if it recieves a bad ip address'''
    monkeypatch.setattr('pings.ping', lambda x: ['line to print'])
    monkeypatch.setattr('pings.ip_address', lambda x: raise_(Exception('foobar')))
    element = get_element
    value = 'Success'
    with pytest.raises(Exception):
        assert send_pings(element, value)
        