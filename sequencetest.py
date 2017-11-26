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
        x = 'AGGCTATCACYYYYQQQQXYZGACTGACCXXXXXXXXXTCCAGGCCGATGCCCXXR'
        y = 'TAGCTATCACYYYYQQQQXYZGACGACCGCXXXXXXXXXXGGTCGATTTGCCCGACX'

        # x = 'ACAGATTA'
        # y = 'TAGCTTA'

        # x = 'PAACGGGCQ'
        # y = 'ACAGGGCQT'

        # f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
        f = self.create_cost_function()
        # xij, yij = self.s.local_alignment_path(x, y, f)
        p = list()
        # self.s.dac(xij, yij, f, p)
        self.s.dac(x, y, f, p)

        print(self.s.r1)
        print(self.s.r2)

        # res1 = self.s.local_alignment(x, y, f)
        # res2 = self.s.local_alignment(list(reversed(x)), list(reversed(y)), f)

        # print("Alignment 1")
        # sequence.StringTool.print_matrix(res1)
        # print("Alignment 2")
        # sequence.StringTool.print_matrix(res2)

        #
        # p = list()
        # self.s.dac(xij, yij, f, p)
        #
        # print(self.s.r1)
        # print(self.s.r2)

    # def test_alignment_linear_with_path(self):
    #     x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
    #     y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
    #     # x = 'ACAGATTA'
    #     # y = 'TAGCTTA'
    #
    #     # f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #     f = self.create_cost_function()
    #     p = list()
    #     self.s.dac(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

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

    # def test_dac_unpack_paths(self):
        # x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
        # y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'

        # x = 'ACAGATTA'
        # y = 'TAGCTTA'
        #
        # f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
        #
        # align = sequence.StringTool.alignment(x, y, f)
        #
        # print()

        # r1 = ""
        # r2 = ""
        # r1, r2 = sequence.StringTool.unpack_alignment(align, x, y, r1, r2)

        # p = list()
        # sequence.StringTool.unpack_paths(align, len(x), len(y), p)
        #
        # print(p)

        # print('Edit Distance: ' + str(align[-1][-1][0]))
        # print('s1: ' + r1)
        # print('s2: ' + r2)
        # print()

    # def test_alignment(self):
    #     # x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
    #     # y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
    #
    #     x = 'ACAGATTA'
    #     y = 'TAGCTTA'
    #
    #     f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #
    #     align = sequence.StringTool.alignment(x, y, f)
    #
    #     print()
    #     sequence.StringTool.print_matrix(align)
    #
    #     r1 = ""
    #     r2 = ""
    #     r1, r2 = sequence.StringTool.unpack_alignment(align, x, y, r1, r2)
    #
    #     # print('Edit Distance: ' + str(align[-1][-1][0]))
    #     print('s1: ' + r1)
    #     print('s2: ' + r2)
    #     print()

    # def test_alignment_without_path(self):
    #     # x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
    #     # y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
    #
    #     x = 'ACAGATTA'
    #     y = 'TAGCTTA'
    #
    #     f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #
    #     align = sequence.StringTool.alignment(x, y, f)
    #
    #     print(align)

    # def test_alignment_linear(self):
    #     x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
    #     y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
    #     f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #     alignment = sequence.StringTool.alignment_linear(x, y, f)
    #     # print(alignment[-1])
    #     print(alignment)


if __name__ == '__main__':
    unittest.main()
