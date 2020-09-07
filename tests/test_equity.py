import sys
import unittest
import logging

from pysecm.ric import RIC
from pysecm.ric.equity import EquityRIC, PreferredEquityRIC, CommonEquityRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class EquityTests(unittest.TestCase):

    def test_eq_cmn_rics(self):

        rics = ['BBDb.TO', 'VAL.N^G20', 'ABCDE.PK', 'T.N', 'AAPL.OQ', 'IIPu.TO']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(CommonEquityRIC.is_valid_str(ric))
            self.assertTrue(EquityRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertFalse(PreferredEquityRIC.is_valid_str(ric))
            self.assertEqual(CommonEquityRIC.from_str(ric), RIC.from_str(ric))
            self.assertEqual(CommonEquityRIC.from_str(ric), EquityRIC.from_str(ric))


    def test_eq_pfd_rics(self):

        rics = ['BBD_pb.TO', 'ENB_pfe.TO', 'C_pp.N']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(PreferredEquityRIC.is_valid_str(ric))
            self.assertTrue(EquityRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertFalse(CommonEquityRIC.is_valid_str(ric))
            self.assertEqual(PreferredEquityRIC.from_str(ric), RIC.from_str(ric))
            self.assertEqual(PreferredEquityRIC.from_str(ric), EquityRIC.from_str(ric))

    def test_eq_rics_malformed(self):

        rics = ['BBDbb.TO', 'VAL.N^A20', 'ABCDEF.PK', '.N', 'AAPL', 'BBD_p.TO', 'ENB_pfee.TO', 'C_a.N', 'USDCAD']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(EquityRIC.is_valid_str(ric))
            self.assertFalse(CommonEquityRIC.is_valid_str(ric))
            self.assertFalse(PreferredEquityRIC.is_valid_str(ric))

