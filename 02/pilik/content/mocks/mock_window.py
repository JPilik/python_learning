'''A mock for the window class within pysimplegui'''
from mocks.mock_element import Element

class Window(dict):
    '''Window class that extends the ditionary class'''
    def __init__(self):
        self['-IN-'] = Element()

    
    def __setitem__(self, key, value):
        '''class required due to inheriting froma dictionary as a base class'''
        key = key.upper()
        super().__setitem__(key, value)

    def disappear(self):
        '''mock implementation of the disappear method'''
        pass

    def reappear(self):
        '''mock implementation of the reappear method'''
        pass

    def read(self):
        '''mock implementation of the read method'''
        return ("Exit", "")
    
    def close(self):
        return True