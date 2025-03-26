import unittest
import freedom

class TestFreedom(unittest.TestCase):
    def test_degreesF(self):
        self.assertEqual(freedom.degreesF(22), 72)

    def test_bananas(self):
        self.assertEqual(round(freedom.bananas(55)), 3)

if __name__ == '__main__':
    unittest.main()
