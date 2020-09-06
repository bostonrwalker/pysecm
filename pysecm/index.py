import re
from datetime import date

from pysecm import Instrument


class Index(Instrument):

    # Regex
    _re_ric = r'^\.[A-Z][A-Z0-9]{1,15}$'  # Respect legacy 17-character RIC limit

    def __init__(self, ric: str, asof_date: (date, None) = None):
        if not Index._is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric, asof_date=asof_date)

    @classmethod
    def _from_ric(cls, ric: str, asof_date: (date, None) = None) -> object:
        return Index(ric=ric, asof_date=asof_date)

    @classmethod
    def _is_valid_ric(cls, ric: str) -> bool:
        return re.match(Index._re_ric, ric) is not None
