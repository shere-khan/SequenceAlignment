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

    def test_local_alignment_200(self):
        f = self.create_cost_function()

        l = 100
        x = sequence.StringTool.sequence_generator(l, 'ACTG')
        y = sequence.StringTool.sequence_generator(l, 'ACTG')

        print('x: ' + ''.join(x))
        print('y: ' + ''.join(y))

        p = list()

        xij, yij = self.s.local_alignment_path(x, y, f)

        self.s.dac(xij, yij, f, p)

        print(self.s.r1)
        print(self.s.r2)

    # def test_alignment_global(self):
    #     f = self.create_cost_function()
    #     l = 6
    #
    #     x = 'TTTCTT'
    #     y = 'AGTCGA'
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #
    #     self.s.dac(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    # def test_alignment_global_horiz(self):
    #     f = self.create_cost_function()
    #     l = 6
    #
    #     x = 'TTTCTT'
    #     y = 'AGTCGA'
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #
    #     self.s.dac_horiz(x, y, f, p)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    # def test_alignment_global_5000(self):
    #     f = self.create_cost_function()
    #     l = 6
    #
    #     x = 'TTTCTT'
    #     y = 'AGTCGA'
    #
    #     # x = 'TTCTTT'
    #     # y = 'AGC'
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #     M = self.s.alignment_matrix(x, y, f)
    #     self.s.print_matrix(M)
    #
    #     r1, r2 = self.s.unpack_alignment(M, x, y, "", "")
    #
    #     print(r1)
    #     print(r2)
    #
    #     print(self.s.r1)
    #     print(self.s.r2)


if __name__ == '__main__':
    unittest.main()
