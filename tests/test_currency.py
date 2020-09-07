import sys
import unittest
import logging

from pysecm.ric import RIC
from pysecm.ric.fx import CurrencyRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class CurrencyTests(unittest.TestCase):

    def test_ccy_rics(self):

        rics = ['USDCAD', 'CADUSD', 'USDJPY']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(CurrencyRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertEqual(CurrencyRIC(ric), RIC(ric))

    def test_ccy_rics_malformed(self):

        rics = ['USDUSD', 'USDCA', 'CADCAD', 'JPYUSA', 'RY.TO', 'C.N', 'foo', 'ABCUSD']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(CurrencyRIC.is_valid_str(ric))
