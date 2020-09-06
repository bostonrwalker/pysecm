import re
from datetime import date

from pysecm import FixedIncome


class Government(FixedIncome):

    # Regex
    _re_ric_govt_ticker = r'[A-Z]{3,4}'
    _re_ric_govt_tbill_code = r'BILL'
    _re_ric = rf'^{_re_ric_govt_ticker}\s({FixedIncome._re_ric_coupon_rate}\s|{_re_ric_govt_tbill_code}\s)?' \
              rf'{FixedIncome._re_ric_maturity_dt}$'

    def __init__(self, ric: str, asof_date: (date, None) = None):
        if not Government._is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric, asof_date=asof_date)

    @classmethod
    def _from_ric(cls, ric: str, asof_date: (date, None) = None) -> object:
        return Government(ric=ric, asof_date=asof_date)

    @classmethod
    def _is_valid_ric(cls, ric: str) -> bool:
        return re.match(Government._re_ric, ric) is not None
