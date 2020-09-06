import logging
import sys
import unittest

from pysecm import Instrument

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class InstrumentTests(unittest.TestCase):

    def test_from_rics(self):

        rics = ['RY.TO', 'RY_pa.TO', 'USDCAD', '.VIX', 'CLc1', 'SIZ0', 'NG']

        for ric in rics:
            print(Instrument.from_ric(ric))
