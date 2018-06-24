from __future__ import print_function
import logging

import smbus2 as smbus

from .utils import get_bus_number


class Component(object):
    ''' Base class for component '''
    _DEBUG = False
    _DEBUG_INFO = 'DEBUG "Component":'
    logger = None

    def __init__(self, debug=False, *args, **kwargs):
        if 'logger' in kwargs:
            self.logger = kwargs.pop('logger')
        if not self.logger:
            self.logger = logging.getLogger(self.__class__.__name__)
        self._DEBUG = debug

    def log(self, *args, **kwargs):
        ''' Print debug info '''
        self.logger.log(*args, **kwargs)

    def debug(self, *args, **kwargs):
        ''' Print debug info '''
        self.logger.debug(*args, **kwargs)


class BusModule(Component):
    ''' Base class for bus component '''
    _DEBUG_INFO = 'DEBUG "BusComponent":'

    def __init__(self, bus_number=None, address=None, debug=False):
        self._DEBUG = debug
        self.address = address
        if bus_number is None:
            bus_number = get_bus_number()
        self.bus_number = bus_number
        self.bus = smbus.SMBus(self.bus_number)
