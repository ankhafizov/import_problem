import unittest

from anvarmod.summator import sum_array


class TestSummator(unittest.TestCase):
    def test_sum(self):
        arr = [1, 2, 3]
        self.assertEqual(sum_array(arr), 6)
