import unittest

from alignment import sequence


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

    # def test_local_alignment_200(self):
    #     f = self.create_cost_function()
    #
    #     l = 100
    #     x = sequence.StringTool.sequence_generator(l, 'ACTG')
    #     y = sequence.StringTool.sequence_generator(l, 'ACTG')
    #
    #     print('x: ' + ''.join(x))
    #     print('y: ' + ''.join(y))
    #
    #     p = list()
    #
    #
    #     print(self.s.r1)
    #     print(self.s.r2)

    def test_alignment_global_5000(self):
        f = self.create_cost_function()

        for i in range(10):
            l = 100
            x = sequence.StringTool.sequence_generator(l, 'ACTG')
            y = sequence.StringTool.sequence_generator(l, 'ACTG')

            # x = 'CTCGCATT'
            # y = 'AGGCGGTA'

            print()
            print('x: ' + ''.join(x))
            print('y: ' + ''.join(y))

            p = list()
            # self.s.dac(x, y, f, p)

            # print('GLOBAL')
            # print(self.s.r1)
            # print(self.s.r2)

            self.s.r1 = ''
            self.s.r2 = ''
            xij, yij = self.s.local_alignment_path(x, y, f)

            self.s.dac(xij, yij, f, p)

            print()
            print('LOCAL')
            print(self.s.r1)
            print(self.s.r2)
            print()


if __name__ == '__main__':
    unittest.main()
