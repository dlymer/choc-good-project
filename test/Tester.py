import unittest
from first import myAppToTest


class Tester(unittest.TestCase):

    def setUp(self):
        self.myApp = myAppToTest()

    def test_add(self):
        self.assertEqual(self.myApp.add(1, 2), 3)

    def test_is_x_equal_to_foos(self):
        self.assertEqual(self.myApp.x, 'foo')


if __name__ == '__main__':
    unittest.main()