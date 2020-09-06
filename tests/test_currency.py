import sys
import unittest
import logging

from pysecm import Currency, Instrument

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class CurrencyTests(unittest.TestCase):

    def test_ccy_rics(self):

        rics = ['USDCAD', 'CADUSD', 'USDJPY']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(Currency.is_valid_ric(ric))
            self.assertTrue(Instrument.is_valid_ric(ric))
            self.assertEqual(Currency.from_ric(ric), Instrument.from_ric(ric))

    def test_ccy_rics_malformed(self):

        rics = ['USDUSD', 'USDCA', 'CADCAD', 'JPYUSA', 'RY.TO', 'C.N', 'foo', 'ABCUSD']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(Currency.is_valid_ric(ric))