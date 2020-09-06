import sys
import unittest
import logging

from pysecm import Equity, PreferredEquity, CommonEquity, Instrument

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class EquityTests(unittest.TestCase):

    def test_eq_cmn_rics(self):

        rics = ['BBDb.TO', 'VAL.N^G20', 'ABCDE.PK', 'T.N', 'AAPL.OQ', 'IIPu.TO']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(CommonEquity.is_valid_ric(ric))
            self.assertTrue(Equity.is_valid_ric(ric))
            self.assertTrue(Instrument.is_valid_ric(ric))
            self.assertFalse(PreferredEquity.is_valid_ric(ric))
            self.assertEqual(CommonEquity.from_ric(ric), Instrument.from_ric(ric))
            self.assertEqual(CommonEquity.from_ric(ric), Equity.from_ric(ric))


    def test_eq_pfd_rics(self):

        rics = ['BBD_pb.TO', 'ENB_pfe.TO', 'C_pp.N']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(PreferredEquity.is_valid_ric(ric))
            self.assertTrue(Equity.is_valid_ric(ric))
            self.assertTrue(Instrument.is_valid_ric(ric))
            self.assertFalse(CommonEquity.is_valid_ric(ric))
            self.assertEqual(PreferredEquity.from_ric(ric), Instrument.from_ric(ric))
            self.assertEqual(PreferredEquity.from_ric(ric), Equity.from_ric(ric))

    def test_eq_rics_malformed(self):

        rics = ['BBDbb.TO', 'VAL.N^A20', 'ABCDEF.PK', '.N', 'AAPL', 'BBD_p.TO', 'ENB_pfee.TO', 'C_a.N', 'USDCAD']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(Equity.is_valid_ric(ric))
            self.assertFalse(CommonEquity.is_valid_ric(ric))
            self.assertFalse(PreferredEquity.is_valid_ric(ric))

