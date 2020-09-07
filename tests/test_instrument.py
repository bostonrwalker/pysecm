import logging
import sys
import unittest

from pysecm import BaseRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class InstrumentTests(unittest.TestCase):

    def test_from_rics(self):

        rics = ['RY.TO', 'RY_pa.TO', 'USDCAD', '.VIX', 'CLc1', 'SIZ0', 'NG', 'UST BILL 03-DEC-2020',
                'CAGV 0.500 01-SEP-2025']
        instruments = [BaseRIC.from_str(ric) for ric in rics]

        for instrument in instruments:
            print('{: <40} {: <40}'.format(str(instrument), repr(instrument)))
