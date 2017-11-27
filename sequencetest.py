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

    # def test_local_alignment_200(self):
    #     f = self.create_cost_function()
    #
    #     file = open("input2.txt", 'r')
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

    # def test_local_alignment_2000(self):
    #     f = self.create_cost_function()
    #
    #     file = open("input5.txt", 'r')
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

    # def test_alignment_global_small_sequence(self):
    #     x = 'AGGCTATCACYYYYQQQQXYZGACTGACCXXXXXXXXXTCCAGGCCGATGCCCXXR'
    #     y = 'TAGCTATCACYYYYQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACX'
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

    # def test_alignment_global_1000(self):
    #     f = self.create_cost_function()
    #
    #     file = open("input3.txt", 'r')
    #     x = file.readline()
    #     y = file.readline()
    #
    #     file.close()
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #     self.s.dac(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    # def test_alignment_global_5000(self):
    #     f = self.create_cost_function()
    #
    #     file = open("input4.txt", 'r')
    #     x = file.readline()
    #     y = file.readline()
    #
    #     file.close()
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #     self.s.dac(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)


if __name__ == '__main__':
    unittest.main()
