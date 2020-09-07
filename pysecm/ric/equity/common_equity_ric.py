import re

from pysecm.ric.equity.equity_ric import EquityRIC


class CommonEquityRIC(EquityRIC):

    # Regex
    _re_ric = rf'^{EquityRIC._re_ric_ticker}({EquityRIC._re_ric_cmn_suffix})?{EquityRIC._re_ric_exch_code}' \
              rf'({EquityRIC._re_ric_delisted_month})?$'

    def __init__(self, ric_str: str):
        if not CommonEquityRIC._is_valid_str(ric_str):
            raise ValueError(f'Invalid RIC - "{ric_str}"')
        super().__init__(ric_str=ric_str)

    @classmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        return re.match(CommonEquityRIC._re_ric, ric_str) is not None
