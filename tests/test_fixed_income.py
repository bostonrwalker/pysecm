import sys
import unittest
import logging

from pysecm.ric import RIC
from pysecm.ric.fixed_income import GovernmentRIC, FixedIncomeRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestFixedIncome(unittest.TestCase):

    def test_fi_govt_rics(self):

        rics = [
            'CAGV 0.500 01-SEP-2025',   # Canada 5 year bonds
            'CAGV 01-OCT-2020',         # Canada 1 month bills (zero coupon)
            'UST BILL 03-DEC-2020',     # US 3 month T-bills (zero coupon)
            'GBGV 4.750 07-DEC-2030',   # UK 10 year bonds
            'UST 1.375 15-AUG-2050',    # US 30-year T-bonds
            'UST 7.250 15-AUG-2020',    # US T-bonds 15 Aug 2020
            'RUGV 7.400 07-DEC-2022',   # Russian Federation 2 year bonds
            'DEGV 15-AUG-2030',         # Germany 10 year Euro-denominated bonds
            'BRGV 01-OCT-2021',         # Brazil 1 year bonds
        ]

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(GovernmentRIC.is_valid_str(ric))
            self.assertTrue(FixedIncomeRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertEqual(GovernmentRIC(ric), RIC(ric))

    def test_fi_govt_rics_malformed(self):

        rics = ['UST BILL 32-DEC-2020', 'UST BILL 1-DEC-2020', 'UST BILL 00-DEC-2020', 'UST BILL 01-ABC-2020',
                'UST 0.700 01-JAN-2999', 'UST 7.0 03-DEC-2020', 'UST BILL', 'US BILL 03-DEC-2020',
                '.SPX', 'USDCAD', 'RY.TO', 'CLCc1']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(GovernmentRIC.is_valid_str(ric))
