import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

    def test_alignment(self):
        # x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
        # y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'

        x = 'ACAGATTA'
        y = 'TAGCTTA'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 0

        align = sequence.StringTool.alignment_matrix(x, y, f)

        print()
        sequence.StringTool.print_matrix(align)

        r1 = ""
        r2 = ""
        r1, r2 = sequence.StringTool.unpack_alignment(align, x, y, r1, r2)

        # print('Edit Distance: ' + str(align[-1][-1][0]))
        print('s1: ' + r1)
        print('s2: ' + r2)
        print()

    def test_alignment_linear_with_path(self):
        # x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
        # y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
        x = 'ACAGATTA'
        y = 'TAGCTTA'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
        p = list()
        sequence.StringTool.dac(x, y, f, p)

        # print(p)

    # def test_alignment_linear(self):
    #     x = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
    #     y = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'
    #     f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #     alignment = sequence.StringTool.alignment_linear(x, y, f)
    #     # print(alignment[-1])
    #     print(alignment)


if __name__ == '__main__':
    unittest.main()
