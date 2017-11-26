import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

    # def test_alignment_linear_number(self):
    #     x = 'AGGCTATCACYYYYQQQQXYZGACTGACCXXXXXXXXXTCCAGGCCGATGCCCXXR'
    #     y = 'TAGCTATCACYYYYQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACX'
    #     # x = 'ACAGATTA'
    #     # y = 'TAGCTTA'
    #
    #     # f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #     f = self.create_cost_function()
    #     best = self.s.local_alignment_linear_number(x, y, f)
    #
    #     print(best)

    def test_local_alignment_linear_path(self):
        # x = 'AGGCTATCACYYYYQQQQXYZGACTGACCXXXXXXXXXTCCAGGCCGATGCCCXXR'
        # y = 'TAGCTATCACYYYYQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACX'

        l = 1000
        x = sequence.StringTool.sequence_generator(l, 'ACTG')
        y = sequence.StringTool.sequence_generator(l, 'ACTG')

        print('x: ' + ''.join(x))
        print('y: ' + ''.join(y))

        f = self.create_cost_function()
        p = list()
        self.s.dac(x, y, f, p)

        print(self.s.r1)
        print(self.s.r2)

    @staticmethod
    def create_cost_function():
        mismatch = input('Enter mismatch score: ')
        match = input('Enter match score: ')
        indel = input('Enter insert/delete score: ')

        def cost(x, y, type):
            if type == 'indel':
                if x == '' or y == '':
                    return int(indel)
            if type == 'match-mismatch':
                if x == y:
                    return int(match)
                if x != y:
                    return int(mismatch)

        return cost

if __name__ == '__main__':
    unittest.main()
