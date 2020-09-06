import logging
import sys
import unittest

from pysecm import Instrument

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class InstrumentTests(unittest.TestCase):

    def test_from_rics(self):

        rics = ['RY.TO', 'RY_pa.TO', 'USDCAD', '.VIX', 'CLc1', 'SIZ0', 'NG']
        instruments = [Instrument.from_ric(ric) for ric in rics]

        for instrument in instruments:
            print(str(instrument))
        for instrument in instruments:
            print(repr(instrument))
