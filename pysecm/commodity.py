import re
from datetime import date

from pysecm import Instrument


class Commodity(Instrument):

    # Regex
    _re_ric_ticker = r'1?[A-Z]{1,3}'
    _re_ric_continuation_month = r'c([1-9][0-9]?|1[1-2][0-9]|13[0-4])'
    _re_ric_delivery_month = r'[FGHJKMNQUVXZ][0-9]'
    _re_ric = rf'^{_re_ric_ticker}({_re_ric_continuation_month}|{_re_ric_delivery_month})?$'

    def __init__(self, ric: str, asof_date: (date, None) = None):
        if not Commodity.is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric, asof_date=asof_date)

    @classmethod
    def _from_ric(cls, ric: str, asof_date: (date, None) = None) -> object:
        return Commodity(ric=ric, asof_date=asof_date)

    @classmethod
    def _is_valid_ric(cls, ric: str) -> bool:
        return re.match(Commodity._re_ric, ric) is not None
