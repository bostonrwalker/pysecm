import re

from pysecm import Instrument


class Index(Instrument):

    # Regex
    _re_ric = r'^\.[A-Z][A-Z0-9]{1,15}$'  # Respect legacy 17-character RIC limit

    def __init__(self, ric: str):
        if not Index.is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric)

    @classmethod
    def from_ric(cls, ric: str) -> object:
        return Index(ric=ric)

    @classmethod
    def is_valid_ric(cls, ric: str) -> bool:
        return re.match(Index._re_ric, ric) is not None
