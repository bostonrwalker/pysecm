from abc import abstractmethod
from typing import final


class Instrument(object):

    def __init__(self, ric: str):
        self.ric = ric

    def __str__(self):
        return f'{self.ric} [{self.__class__.__name__}]'

    def __repr__(self):
        return f'{type(self).__module__}.{type(self).__qualname__}' \
               f'{{{",".join(f"{k}={repr(v)}" for k, v, in vars(self).items())}}}'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.ric == other.ric

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_ric(cls, ric: str) -> object:
        """
        Instantiate an instrument from a valid RIC
        :param ric: Reuters Instrument Code
        :return: Instrument
        """
        if len(cls.__subclasses__()) > 0:
            return cls._get_class_by_ric(ric).from_ric(ric)
        else:
            raise AttributeError('from_ric not implemented')

    @classmethod
    def is_valid_ric(cls, ric: str) -> bool:
        """
        Check whether a string is a correctly formatted RIC
        Note: Only checks formatting, does not check whether the RIC belongs to an existing or valid security
        :param ric: Reuters Instrument Code
        """
        if len(cls.__subclasses__()) > 0:
            try:
                Instrument._get_class_by_ric(ric)
                return True
            except ValueError:
                return False
        else:
            raise AttributeError('is_valid_ric not implemented')

    @classmethod
    @final
    def _get_class_by_ric(cls, ric: str):
        matches = [subcls for subcls in cls.__subclasses__() if subcls.is_valid_ric(ric)]
        if len(matches) == 0:
            raise ValueError(f'Invalid RIC - {ric} did not match any known instruments')
        elif len(matches) == 1:
            return matches[0]
        else:
            raise ValueError(f'Ambiguous RIC - {ric} matched multiple known instruments: '
                             f'{" ".join([str(m) for m in matches])}')
