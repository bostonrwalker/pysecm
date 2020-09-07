from abc import ABC, abstractmethod
from typing import final, List, Type
from itertools import chain
import re


class RIC(ABC):
    """
    Class for validating and representing RIC strings
    """

    # Override new method to return subclass
    def __new__(cls, ric_str: str):
        if len(cls.__subclasses__()) > 0:
            # Search recursively for matching subclass
            matches = cls.get_class_by_str(ric_str)
            if len(matches) == 1:
                # If match found, call from_ric
                concrete_cls = matches[0]
            elif len(matches) == 0:
                raise ValueError(f'Invalid RIC string - "{ric_str}" did not match any known instruments')
            else:
                raise ValueError(f'Ambiguous RIC string - "{ric_str}" matched multiple known instruments: '
                                 f'{" ".join([str(m) for m in matches])}')
        else:
            concrete_cls = cls
        return object.__new__(concrete_cls)

    def __init__(self, ric_str: str):
        """
        :param ric_str: Reuters Instrument Code
        """
        self.__ric_str = ric_str

    def __str__(self):
        return f'{self.ric_str} [{re.sub("RIC$", "", self.__class__.__name__)}]'

    def __repr__(self):
        return f'{type(self).__module__}.{type(self).__qualname__}' \
               f'{{{",".join(f"{k}={repr(v)}" for k, v, in vars(self).items())}}}'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.ric_str == other.ric_str

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.ric_str)
    
    @property
    def ric_str(self):
        """
        :return: Reuters Instrument Code
        """
        return self.__ric_str

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
