'''Function for pinging targets'''
from pythonping import ping
from element_printer import print_w, printerror_w
import ipaddress

'''Sends pings results to a given element'''
def send_pings(element, value):
    try:
        ip = ipaddress.ip_address(str.strip(value))
        addy = str.strip(value)
        for result in ping(addy):
            print_w(result, element)
    except ValueError:
        printerror_w(f'{str.strip(value)} is not a valid IP address.', element)
    