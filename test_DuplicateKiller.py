import unittest
from duplicates import duplicatekiller


class TestDuplicateKiller(unittest.TestCase):
    def test_del_duplicates(self):
        self.assertEqual(duplicatekiller([0, 1, 1, 2, 2, 2, 3, 3, 3, 3]), [0, 1, 2, 3])
        self.assertEqual(duplicatekiller([8, 7, 12, 1, 4, 5, 5, 7, 9, 6, 8]), [8, 7, 12, 1, 4, 5, 9, 6])
        self.assertEqual(duplicatekiller([1]), [1])
        self.assertEqual(duplicatekiller([1, 2, 3]), [1, 2, 3])
