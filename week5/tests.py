# Mateo Estrada Jorge
# Software Engineering II
# Random Testing
# Goals:
# 1. Pratice writing random tests
# 2. Pratice trying to diagnose the cause of the discovered bugs

from credit_card_validator import credit_card_validator
import unittest
import random


class TestCase(unittest.TestCase):

    def test_bug1(self):
        # Testing visa stuff
        tests_to_generate = 100000
        # generate random tests
        for i in range(0, tests_to_generate):
            visa_pre = 4
            # Get the length of the card
            visa = self.make_card_num(16, visa_pre)
            credit_card_validator(visa)

    def test_bug2(self):
        tests_to_generate = 100000
        for i in range(0, tests_to_generate):
            master_card_pre = [34, 37]
            prefix = random.choice(master_card_pre)
            master_card = self.make_card_num(16, prefix)
            credit_card_validator(master_card)

    def test_bug3(self):
        tests_to_generate = 10000
        for i in range(0, tests_to_generate):
            amer_expr_pre = [51, 52, 53, 54, 54]
            prefix = random.choice(amer_expr_pre)
            amer_card = self.make_card_num(15, prefix)
            credit_card_validator(amer_card)

    def test_bug4(self):
        tests_to_generate = 10000
        for i in range(0, tests_to_generate):
            amer_expr_pre = [i for i in range(2221, 2720)]
            prefix = random.choice(amer_expr_pre)
            amer_card = self.make_card_num(15, prefix)
            credit_card_validator(amer_card)

    def test_bug5(self):
        tests_to_generate = 100000
        for i in range(0, tests_to_generate):
            card = random.randint(0000000000000000, 9999999999999999)
            credit_card_validator(card)

    def make_card_num(self, length, prefix):
        '''
        Makes the visa card numbers given the test cases
        int: length - length of the card number
        prefix: prefix that goes with the card
        '''
        card = ''
        card += str(prefix)
        for i in range(0, length - len(str(prefix))):
            card += str(random.randint(0, 9))
        print(len(card), card)
        return card


if __name__ == '__main__':
    unittest.main()
