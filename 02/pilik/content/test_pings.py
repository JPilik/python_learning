'''Test module for element_printer_test'''
from pings import send_pings
from mocks.mock_element import Element
import pytest

def test_ping(monkeypatch):
    '''test of the ping function'''
    monkeypatch.setattr('pings.ping', lambda x: {})
    monkeypatch.setattr('pings.ip_address', lambda x: '1.2.3.4')
    
    element = Element()
    value = 'Success'
    result = send_pings(element, value)
    assert True == result

def raise_(ex):
    raise ex

def test_ping_exception(monkeypatch):
    '''test of the ping function'''
    monkeypatch.setattr('pings.ping', lambda x: {})
    monkeypatch.setattr('pings.ip_address', lambda x: raise_(Exception('foobar')))
    
    element = Element()
    value = 'Success'
    with pytest.raises(Exception):
        assert send_pings(element, value)
        