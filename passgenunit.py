import unittest
from pms import *
from hibp import *


class MyTestCase(unittest.TestCase):
    def test_Passcheck(self):
        p = "Yash@123"
        self.assertFalse(pass_Check(p))
        q = "Bu!nTy@123"
        self.assertTrue(pass_Check(q))

    def test_Hibp(self):
        a = "Qwertyuiop"
        self.assertEqual(hibp(a), False)
        b = "Bunty@123#Kotla"
        self.assertEqual(hibp(b), True)

    def test_passgen(self):
        a=""





if __name__ == '__main__':
    unittest.main()
