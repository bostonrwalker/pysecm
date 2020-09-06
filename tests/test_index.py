import sys
import unittest
import logging

from pysecm import Index, Instrument

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class IndexTests(unittest.TestCase):

    def test_index_rics(self):

        rics = ['.SPX', '.VIX6M', '.GSPTSE']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(Index.is_valid_ric(ric))
            self.assertTrue(Instrument.is_valid_ric(ric))
            self.assertEqual(Index.from_ric(ric), Instrument.from_ric(ric))

    def test_index_rics_malformed(self):

        rics = ['SPX', '.1SP', '.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'USDCAD', 'RY.TO']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(Index.is_valid_ric(ric))

