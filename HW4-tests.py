import unittest

from HW2RecForTests import rec
from HW2SortForTests import SelectSort


class MyTestCasesForRecursion(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(rec(3, 3), 1)

    def test_rec_2(self):
        self.assertEqual(rec(5, 1), 5)

    def test_rec_3(self):
        self.assertEqual(rec(5, 4), 5)


class MyTestCasesForSelectSort(unittest.TestCase):
    def test_sort(self):
        A = [1, 6, 4, 8, 4, 9, 2, 3]
        self.assertEqual(SelectSort(A), A.sort())


if __name__ == '__main__':
    unittest.main()
