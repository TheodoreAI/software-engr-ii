# Mateo Estrada Jorge
# October 2021
# Software Engineering II
# Assignment II
# Use white box testing on a function and get the
# tests in 7 or less test cases.
# To figure this out, I turned the conditional statements
# into algebra problems (e.g. val*5 < 361 --> 5x < 361
# and x/2 < 24) and solved for valid range of numbers.
# The most difficult numbers to find were for the last elif.


import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    # def test_c1(self):
    #     val = 0
    #     self.assertEqual(contrived_func(val), True)

    def test_c1(self):
        val = 333
        self.assertFalse(contrived_func(val))

    def test_c2(self):
        val = 125
        self.assertEqual(contrived_func(val), True)

    def test_c3(self):
        val = 6
        self.assertEqual(contrived_func(val), False)

    def test_c4(self):
        val = 280
        self.assertEqual(contrived_func(val), True)

    def test_c5(self):
        val = 9.8
        self.assertEqual(contrived_func(val), True)

    def test_c6(self):
        val = 49
        self.assertEqual(contrived_func(val), False)

    def test_c7(self):
        val = 75
        self.assertEqual(contrived_func(val), True)


if __name__ == '__main__':
    unittest.main()
