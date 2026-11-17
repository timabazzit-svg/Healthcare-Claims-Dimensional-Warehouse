import os
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from main import run

class ProjectTests(unittest.TestCase):
    def setUp(self):
        os.chdir(ROOT)

    def test_representative_sample(self):
        result=run()
        expected={'claims_loaded': 3, 'provider_paid_totals': {'North Clinic': 155.0, 'South Clinic': 120.0}}
        for key,value in expected.items():
            self.assertEqual(result[key],value, f'Mismatch on {key}')

    def test_replay_consistency(self):
        self.assertEqual(run(),run())

if __name__=='__main__':
    unittest.main()
