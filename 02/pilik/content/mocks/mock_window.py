'''A mock for the window class within pysimplegui'''
from mocks.mock_element import Element

class Window(dict):
    '''A mock for the window class within pysimplegui'''
    def __init__(self):
        '''Class initializer'''
        self['-IN-'] = Element()

    
    def __setitem__(self, key, value):
        '''dictionary inheritance requirement'''
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