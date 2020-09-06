import re
from datetime import date

from pysecm.equity import Equity


class CommonEquity(Equity):

    # Regex
    _re_ric = rf'^{Equity._re_ric_ticker}({Equity._re_ric_cmn_suffix})?{Equity._re_ric_exch_code}' \
              rf'({Equity._re_ric_delisted_month})?$'

    def __init__(self, ric: str, asof_date: (date, None) = None):
        if not CommonEquity._is_valid_ric(ric):
            raise ValueError(f'Invalid RIC - {ric}')
        super().__init__(ric=ric, asof_date=asof_date)

    @classmethod
    def _from_ric(cls, ric: str, asof_date: (date, None) = None) -> object:
        return CommonEquity(ric=ric, asof_date=asof_date)

    @classmethod
    def _is_valid_ric(cls, ric: str) -> bool:
        return re.match(CommonEquity._re_ric, ric) is not None
