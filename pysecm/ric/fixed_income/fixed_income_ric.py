from pysecm.ric import RIC


class FixedIncomeRIC(RIC):

    # Regex
    _re_dom = r'(0[1-9]|[1-2][0-9]|3[0-1])'
    _re_mon = r'(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)'
    _re_yr = r'(19[0-9][0-9]|2[0-1][0-9][0-9])'  # Valid range: 1900 - 2199
    _re_ric_maturity_dt = rf'{_re_dom}\-{_re_mon}\-{_re_yr}'
    _re_ric_coupon_rate = r'[1-9]?[0-9]\.[0-9]{3}'

    def __init__(self, ric_str: str):
        super().__init__(ric_str=ric_str)
