import unittest

import sequence


class TestStringAlignment(unittest.TestCase):
    def setUp(self):
        self.s = sequence.StringTool()

    def test_alignment(self):
        s1 = "actgaabxu"
        s2 = "abtaaabxc"
        alignment = self.s.alignment(s1, s2)
        print(alignment)

    def test_alignment_linear(self):
        s1 = "actgaabxu"
        s2 = "abtaaabxc"
        alignment = self.s.alignment_linear(s1, s2)
        print(alignment)


if __name__ == '__main__':
    unittest.main()
