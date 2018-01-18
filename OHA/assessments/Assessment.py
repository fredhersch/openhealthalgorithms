from abc import ABCMeta, abstractmethod

__author__ = 'indrajit'
__email__ = 'eendroroy@gmail.com'


class Assessment(object):
    __metaclass__ = ABCMeta

    __data = {}

    def __init__(self, input_data=None):
        if input_data is not None:
            self.__data = input_data

    def _get_data(self):
        return self.__data

    @abstractmethod
    def assess(self):
        raise NotImplementedError('method not implemented')
