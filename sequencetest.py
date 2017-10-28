import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

    def test(self):
        s1 = "actg"
        s2 = "abta"
        alignment = self.s.alignment(s1, s2)
        print(alignment)
        # print(alignment[0])
        # print(alignment[1])


if __name__ == '__main__':
    unittest.main()
