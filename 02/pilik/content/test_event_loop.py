'''Test module for element_printer_test'''
from event_loop import event_loop

def send_pings():
    pass

class Sg():
    def popup(self, title, version, sgVersionsLabel, sgVersions):
        pass
    
class Window(dict):
    def __setitem__(self, key, value):
         key = key.upper()
         super().__setitem__(key, value)

    def disappear(self):
        pass

    def reappear(self):
        pass

    def read(self):
        return ("Exit", "")
    
    def close(self):
        return True

def test_event_loop():
    '''Test for Event Loop'''
    sg = Sg()
    sg.WIN_CLOSED = 'WIN_CLOSED'
    window = Window()
    result = event_loop(sg, window, lambda x: None, lambda x: None)
    assert result == True