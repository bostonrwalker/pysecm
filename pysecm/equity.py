import re

from pysecm import Instrument


class Equity(Instrument):

    # Regexes
    _re_ric_ticker = r'[A-Z]{1,5}'
    _re_ric_cmn_suffix = r'[a-z]'
    _re_ric_pfd_suffix = r'_pf?[a-z]'
    _re_ric_exch_code = r'\.[A-Z]{1,3}'
    _re_ric_delivery_month = r'[FGHJKMNQUVXZ][0-9]{2}'
    _re_ric_delisted_month = rf'\^{_re_ric_delivery_month}'
    _re_ric = rf'^{_re_ric_ticker}({_re_ric_cmn_suffix}|{_re_ric_pfd_suffix})?{_re_ric_exch_code}' \
              rf'({_re_ric_delisted_month})?$'

    def __init__(self, ric: str):
        super().__init__(ric=ric)

    @classmethod
    def is_valid_ric(cls, ric: str) -> bool:
        return re.match(Equity._re_ric, ric) is not None
