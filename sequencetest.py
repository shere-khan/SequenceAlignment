import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

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

    # def test_local_alignment_50(self):
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

    # def test_local_alignment_50(self):
    #     f = self.create_cost_function()
    #
    #     x = 'AGGCTATCACYYYYQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQAHLFKFAOVUHAIBADALSDKLHBASDGFAVDLABVDKLABKLJDVBALKSD'
    #     y = 'TAGCTATCACYYYYQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACXXXXRRRYZZZ'
    #
    #     print(len(x))
    #     print(len(y))
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #     xij, yij = self.s.local_alignment_path(x, y, f)
    #
    #     self.s.dac(xij, yij, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    def test_local_alignment_200(self):
        f = self.create_cost_function()

        file = open("input2.txt", 'r')
        x = file.readline()
        y = file.readline()

        file.close()

        print('x: ' + ''.join(x))
        print('y: ' + ''.join(y))

        p = list()

        xij, yij = self.s.local_alignment_path(x, y, f)

        self.s.dac(xij, yij, f, p)

        print(self.s.r1)
        print(self.s.r2)

    # def test_local_alignment_400(self):
    #     f = self.create_cost_function()
    #
    #     file = open("input1.txt", 'r')
    #     x = file.readline()
    #     y = file.readline()
    #
    #     file.close()
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #
    #     xij, yij = self.s.local_alignment_path(x, y, f)
    #
    #     self.s.dac(xij, yij, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    # def test_alignment_global_large_number(self):
    #     # x = 'AGGCTATCACYYYYQQQQXYZGACTGACCXXXXXXXXXTCCAGGCCGATGCCCXXR'
    #     # y = 'TAGCTATCACYYYYQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACX'
    #
    #     l = 2000
    #     x = sequence.StringTool.sequence_generator(l, 'ACTG')
    #     y = sequence.StringTool.sequence_generator(l, 'ACTG')
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     f = self.create_cost_function()
    #     p = list()
    #     self.s.dac(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)


if __name__ == '__main__':
    unittest.main()
