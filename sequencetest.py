import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

    def test_alignment_linear(self):
        s1 = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
        s2 = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 0

        alignment = sequence.StringTool.alignment_linear(s1, s2, f)
        # print(alignment[-1])
        print(alignment)

    def test_alignment(self):
        s1 = 'AGGCTATCACCTGACCTCCAGGCCGATGCCCXXR'
        s2 = 'TAGCTATCACGACCGCGGTCGATTTGCCCGACX'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 0

        align = sequence.StringTool.alignment(s1, s2, f)

        print()
        sequence.StringTool.print_matrix(align)

        r1 = ""
        r2 = ""
        r1, r2 = sequence.StringTool.unpack_alignment(align, s1, s2, r1, r2)

        # print('Edit Distance: ' + str(align[-1][-1][0]))
        print('s1: ' + r1)
        print('s2: ' + r2)
        print()

if __name__ == '__main__':
    unittest.main()
