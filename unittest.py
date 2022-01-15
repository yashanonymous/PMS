import unittest
from pms import *
from hibp import *
import csv


class MyTestCase(unittest.TestCase):
    #Checking with Policy
    def test_Passcheck(self):
        p = "Yash@123"
        self.assertFalse(pass_Check(p))
        q = "Bu!nTy@123"
        self.assertTrue(pass_Check(q))

    #HIBP api call whether the password is leaked or not
    def test_Hibp(self):
        a = "Qwertyuiop"
        self.assertEqual(hibp(a), False)
        b = "Bunty@123#Kotla"
        self.assertEqual(hibp(b), True)
    #Checking the passgen function to verify whether the password is generated as per policy
    def test_passgen(self):
        a="suryavanshi"
        self.assertTrue(pass_Check(pass_Gen(a)))

    #Inserting values into database
    def test_db(self):
        self.assertTrue(addAdmin("Superuser", "QWERTYUIOP@1997",))

    #Generating batch of passwords and sending them to database
    def test_batchgen(self):
        y="USERS.csv"
        batch_Gen(y)




if __name__ == '__main__':
    unittest.main()
