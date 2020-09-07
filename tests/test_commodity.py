import sys
import unittest
import logging

from pysecm.ric import RIC
from pysecm.ric.commodity import CommodityRIC

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class CommodityTests(unittest.TestCase):

    def test_cmdty_rics(self):

        rics = [
            'C',    # CBOT corn
            'EMA',  # EURONEXT corn
            'O',    # CBOT oats
            'RR',   # Rough rice
            'S',    # Soybeans
            'RS',   # Rapeseed
            'SM',   # Soybean meal
            'BO',   # Soybean oil
            'W',    # Wheat
            'DCS',  # Milk
            'CC',   # ICE cocoa
            'KC',   # ICE coffee C
            'CT',   # ICE cotton no. 2
            'SB',   # ICE sugar no 11
            'OJ',   # ICE frozen concentrated orange juice
            'CL',   # WTI crude
            'CO',   # Brent
            'ZE',   # CBOT ethanol
            'ZE',  # CBOT ethanol (electronic)
            'NG',   # NYMEX nat gas Henry hub
            'HO',   # Heating oil (NY harbor)
            'RB',   # NYMEX RBOB gasoline
            'HG',   # COMEX copper
            'GC',   # COMEX gold
            'PL',   # NYMEX platinum
            'PA',   # NYMEX palladium
            'SI',   # COMEX silver
            '1SI',  # COMEX silver (electronic)
            'CLF0', 'CLG1', 'CLH2', 'CLJ2', 'CLK3', 'CLM4', 'CLN5', 'CLQ6', 'CLU7', 'CLV8', 'CLX9', 'CLZ0',  # Delivery
            'CLc1', 'CLc99', 'CLc134',  # Continuations
        ]

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertTrue(CommodityRIC.is_valid_str(ric))
            self.assertTrue(RIC.is_valid_str(ric))
            self.assertEqual(CommodityRIC(ric), RIC(ric))

    def test_cmdty_rics_malformed(self):

        rics = ['ABCD', '2RC', 'CLc0', 'NGd8', 'CLA0', 'CLc135', 'AAPL.N', '.SPX', 'USDCAD']

        for ric in rics:
            logging.debug(f'Testing {ric}')
            self.assertFalse(CommodityRIC.is_valid_str(ric))
