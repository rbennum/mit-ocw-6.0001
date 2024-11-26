import unittest
import math
import numpy
import pylab

class TestPSet0(unittest.TestCase):

    def test_power_of(self):
        x = 10
        y = 2
        self.assertEqual(x**y, 100)

    def test_log_base2(self):
        self.assertAlmostEqual(math.log2(10), numpy.log2(10))
        self.assertAlmostEqual(math.log2(10), pylab.log2(10))

if __name__ == '__main__':
    unittest.main()