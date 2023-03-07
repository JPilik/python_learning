'''Test module for element_printer_test'''
from pings import send_pings


def mock_ipaddress(addr):
    return '8.8.8.8'


def test_ping(monkeypatch):
    '''test of the ping function'''
    monkeypatch.setitem(pings.ping, 'ping', lambda x: None)
    result = send_pings(element, value)
