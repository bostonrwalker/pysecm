import re

from pysecm.ric import RIC


class CommodityRIC(RIC):

    # Regex
    _re_ric_ticker = r'1?[A-Z]{1,3}'
    _re_ric_continuation_month = r'c([1-9][0-9]?|1[1-2][0-9]|13[0-4])'
    _re_ric_delivery_month = r'[FGHJKMNQUVXZ][0-9]'
    _re_ric = rf'^{_re_ric_ticker}({_re_ric_continuation_month}|{_re_ric_delivery_month})?$'

    def __init__(self, ric_str: str):
        if not CommodityRIC._is_valid_str(ric_str):
            raise ValueError(f'Invalid RIC - "{ric_str}"')
        super().__init__(ric_str=ric_str)

    @classmethod
    def _from_str(cls, ric_str: str) -> object:
        return CommodityRIC(ric_str=ric_str)

    @classmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        return re.match(CommodityRIC._re_ric, ric_str) is not None
