'''Function for pinging targets'''
from ipaddress import ip_address
from pythonping import ping
from element_printer import print_w, printerror_w

def send_pings(element, value):
    '''Sends pings results to a given element'''
    try:
        ip_address(str.strip(value))
        addy = str.strip(value)
        for result in ping(addy):
            print_w(result, element)
    except ValueError:
        printerror_w(f'{str.strip(value)} is not a valid IP address.', element)
    return True
    