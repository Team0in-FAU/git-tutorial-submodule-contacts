from .addresses.addresses import *

def create_contact(name):
    return "Name: {}, Address: {}".format(name, get_address(name))
