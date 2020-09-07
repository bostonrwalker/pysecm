from abc import ABC, abstractmethod
from typing import final, List, Type
from itertools import chain
import re


class RIC(ABC):
    """
    Class for validating and representing RIC strings
    """

    def __init__(self, ric_str: str):
        """
        :param ric_str: Reuters Instrument Code
        """
        self.ric_str = ric_str

    def __str__(self):
        return f'{self.ric_str} [{re.sub("RIC$", "", self.__class__.__name__)}]'

    def __repr__(self):
        return f'{type(self).__module__}.{type(self).__qualname__}' \
               f'{{{",".join(f"{k}={repr(v)}" for k, v, in vars(self).items())}}}'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.ric_str == other.ric_str

    def __ne__(self, other):
        return not self == other

    @classmethod
    @final
    def from_str(cls, ric_str: str) -> 'RIC':
        """
        Instantiate a RIC from a valid RIC string
        :param ric_str: Reuters Instrument Code
        :return: Instrument
        """
        try:
            # If _from_ric is defined for this class, use _from_ric
            return cls._from_str(ric_str)
        except AttributeError:
            # Otherwise, search recursively for matching subclass
            matches = cls.get_class_by_str(ric_str)
            if len(matches) == 1:
                # If match found, call from_ric
                return matches[0].from_str(ric_str)
            elif len(matches) == 0:
                raise ValueError(f'Invalid RIC string - "{ric_str}" did not match any known instruments')
            else:
                raise ValueError(f'Ambiguous RIC string - "{ric_str}" matched multiple known instruments: '
                                 f'{" ".join([str(m) for m in matches])}')

    @classmethod
    @abstractmethod
    def _from_str(cls, ric_str: str) -> 'RIC':
        """
        Return an instrument
        If not implemented, from_ric will search recursively for a matching subclass using get_class_by_ric and call
        from_ric on the subclass
        Must be implemented for concrete types
        :param ric: Reuters Instrument Code
        :return: Instrument
        """
        raise AttributeError('Abstract class method _from_ric not defined')

    @classmethod
    @final
    def get_class_by_str(cls, ric_str: str) -> List[Type['RIC']]:
        """
        Return a list of Instrument subclasses matching the formatting of a given RIC
        If _get_class_by_ric is not implemented, calls itself recursively for subclasses
        If no subclasses, will use _is_valid_ric to determine whether to return class or empty list
        :param ric_str: Reuters Instrument Code
        :return: List of matching Instrument types
        """
        try:
            # If _get_class_by_ric is defined for this class, use _get_class_by_ric
            return cls._get_class_by_str(ric_str)
        except AttributeError:
            # Otherwise, use recursive definition for subclasses...
            if len(cls.__subclasses__()) > 0:
                return list(chain(*[subcls.get_class_by_str(ric_str) for subcls in cls.__subclasses__()]))
            else:
                # ...or _is_valid_ric if there are no subclasses defined
                return [cls] if cls._is_valid_str(ric_str) else []

    @classmethod
    def _get_class_by_str(cls, ric_str: str) -> List[Type['RIC']]:
        """
        Return a list of Instrument subclasses matching the formatting of a given RIC
        If not implemented, get_class_by_ric will call itself recursively on subclasses
        If not implemented for concrete types, _is_valid_ric will be called
        :param ric_str: Reuters Instrument Code
        :return: List of matching Instrument types
        """
        raise AttributeError('Abstract class method _get_class_by_str not defined')

    @classmethod
    @final
    def is_valid_str(cls, ric_str: str) -> bool:
        """
        Check whether a string is a correctly formatted RIC
        Note: Only checks formatting, does not check whether the RIC belongs to an existing or valid security
        :param ric_str: Reuters Instrument Code
        """
        try:
            # If _is_valid_ric is defined for this class, use _is_valid_ric
            return cls._is_valid_str(ric_str)
        except AttributeError:
            # Otherwise, use recursive definition
            matches = [subcls for subcls in cls.__subclasses__() if subcls.is_valid_str(ric_str)]
            return len(matches) == 1

    @classmethod
    @abstractmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        """
        Check whether a string is a correctly formatted RIC (non-recursive definition)
        If not implemented, _is_valid_ric will call itself recursively on subclasses
        Must be implemented for concrete types
        :param ric_str: Reuters Instrument Code
        """
        raise AttributeError('Abstract class method _is_valid_str not defined')
