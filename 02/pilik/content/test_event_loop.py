'''Test module for element_printer_test'''
import pytest
from event_loop import event_loop
from mocks.mock_sg import Sg
from mocks.mock_window import Window

@pytest.fixture(name="get_sg")
def fixture_sg():
    '''Fixture to return the PySimpleGUI object'''
    return Sg()

@pytest.fixture(name="get_window")
def fixture_window():
    '''Fixture to return the PySimpleGUI Window'''
    return Window()

def test_event_loop_for_close(get_sg, get_window):
    '''Test for Event Loop'''
    s_g = get_sg
    window = get_window
    result = event_loop(s_g, window)
    assert result is True

def test_event_loop_for_ping(get_sg, get_window):
    '''Test for Event Loop for a ping'''
    s_g = get_sg
    window = get_window
    window.read = lambda : ("Ping", ['Test', ''])
    result = event_loop(s_g, window)
    assert result is True

def test_event_loop_for_about(get_sg, get_window):
    '''Test for Event Loop for a ping'''
    s_g = get_sg
    window = get_window
    window.read = lambda : ("About...", ['Test', ''])
    result = event_loop(s_g, window)
    assert result is True
