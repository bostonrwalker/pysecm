import re
from iso4217 import Currency as iso4217_Currency

from pysecm.ric import RIC


class CurrencyRIC(RIC):

    # Regex
    _re_iso4217 = r'[A-Z]{1,3}'
    _re_ric = rf'^{_re_iso4217}{_re_iso4217}$'

    def __init__(self, ric_str: str):
        if not CurrencyRIC._is_valid_str(ric_str):
            raise ValueError(f'Invalid RIC - "{ric_str}"')
        super().__init__(ric_str=ric_str)

    @classmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        if re.match(CurrencyRIC._re_ric, ric_str) is None:
            return False
        try:
            base, quote = iso4217_Currency(ric_str[0:3]), iso4217_Currency(ric_str[3:6])
        except ValueError:
            return False
        if base == quote:
            return False
        return True
