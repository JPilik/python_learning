'''Test module for element_printer_test'''
import pytest
from mocks.mock_sg import Sg
from main import main

@pytest.fixture(name="get_sg")
def fixture_sg():
    '''Test to Mock the PySimpleGUI primary libary'''
    return Sg()



def test_main(monkeypatch, get_sg):
    '''Test for main funciton'''
    s_g = get_sg
    monkeypatch.setattr('main.sg', s_g)
    assert main() is True
    