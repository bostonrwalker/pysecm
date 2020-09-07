import re

from pysecm.ric import RIC


class IndexRIC(RIC):

    # Regex
    _re_ric = r'^\.[A-Z][A-Z0-9]{1,15}$'  # Respect legacy 17-character RIC limit

    def __init__(self, ric_str: str):
        if not IndexRIC._is_valid_str(ric_str):
            raise ValueError(f'Invalid RIC - "{ric_str}"')
        super().__init__(ric_str=ric_str)

    @classmethod
    def _is_valid_str(cls, ric_str: str) -> bool:
        return re.match(IndexRIC._re_ric, ric_str) is not None
