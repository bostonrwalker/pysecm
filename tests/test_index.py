import sys
import unittest
import logging

from pysecm.ric import RIC
from pysecm.ric.index import IndexRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class IndexTests(unittest.TestCase):

    def test_index_rics(self):

        rics = ['.SPX', '.VIX6M', '.GSPTSE']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(IndexRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertEqual(IndexRIC.from_str(ric), RIC.from_str(ric))

    def test_index_rics_malformed(self):

        rics = ['SPX', '.1SP', '.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'USDCAD', 'RY.TO']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(IndexRIC.is_valid_str(ric))

