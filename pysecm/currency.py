import re
from iso4217 import Currency as iso4217_Currency

from pysecm import Instrument


class Currency(Instrument):

    # Regex
    _re_iso4217 = r'[A-Z]{1,3}'
    _re_ric = rf'^{_re_iso4217}{_re_iso4217}$'

    def __init__(self, ric: str):
        if not Currency.is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric)

    @classmethod
    def _from_ric(cls, ric: str) -> object:
        return Currency(ric=ric)

    @classmethod
    def _is_valid_ric(cls, ric: str) -> bool:
        if re.match(Currency._re_ric, ric) is None:
            return False
        try:
            base, quote = iso4217_Currency(ric[0:3]), iso4217_Currency(ric[3:6])
        except ValueError:
            return False
        if base == quote:
            return False
        return True
