from  unittest import TestCase
import unittest

class myTestOne(TestCase):
    def test_one(self):
        self.assertTrue(100 > 900 , "Shoul be True")
    def test_two(self):
        self.assertEqual(40+60 , 100 , "should be 100")


if __name__ == "__main__":
    unittest.main()