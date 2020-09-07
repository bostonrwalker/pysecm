import re

from pysecm.ric.fixed_income import FixedIncomeRIC


class GovernmentRIC(FixedIncomeRIC):

    # Regex
    _re_ric_govt_ticker = r'[A-Z]{3,4}'
    _re_ric_govt_tbill_code = r'BILL'
    _re_ric = rf'^{_re_ric_govt_ticker}\s({FixedIncomeRIC._re_ric_coupon_rate}\s|{_re_ric_govt_tbill_code}\s)?' \
              rf'{FixedIncomeRIC._re_ric_maturity_dt}$'

    def __init__(self, ric_str: str):
        if not GovernmentRIC._is_valid_str(ric_str):
            raise ValueError(f'Invalid RIC - "{ric_str}"')
        super().__init__(ric_str=ric_str)

    @classmethod
    def _from_str(cls, ric_str: str) -> object:
        return GovernmentRIC(ric_str=ric_str)

    @classmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        return re.match(GovernmentRIC._re_ric, ric_str) is not None
