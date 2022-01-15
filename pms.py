import csv
from datetime import date
import string
import random
import json
import hibp

#Database Configuration
import mysql.connector
with open('db.json') as crd:
    db=json.load(crd)
    mydb = mysql.connector.connect(
        host=db['Host'],
        user=db['User'],
        password=db['Password'],
        port=db['Port'],
        database=db['Database']
    )

d=date.today()
Mycursor=mydb.cursor()

# policy file
"https://www.w3schools.com/python/python_json.asp"
with open('policy.json') as policy:
    r=json.load(policy)


Lower = r['Lowercase']
Upper = r['Uppercase']
Chars = r['Characters']
Digits = r['Digits']
Minlen = r['Min_len']
DateOfMod = r['DateofMod']
change = r['PolicyChange']

'''Count the Number of matching characters in a pair of string Geeks for Geeks'''
"https://www.geeksforgeeks.org/python-count-the-number-of-matching-characters-in-a-pair-of-string/"


def count(str1, str2):
    set_string1 = set(str1)
    set_string2 = set(str2)
    counted = set_string1 & set_string2
    return len(counted)

def addAdmin(a,b):
    Mycursor.execute('''Insert Into Access_table(id,Pass,Access,Date) Values(%s,%s,%s,%s)''',
                     (a, b, "ADMIN", DateOfMod,))
    mydb.commit()
    return True


# Verifying password with policy
def pass_Check(x):
    a = x

    up = count(a, string.ascii_uppercase)
    low = count(a, string.ascii_lowercase)
    punct = count(a, string.punctuation)
    dig = count(a, string.digits)

    if (Upper <= up and Lower <= low and Chars <= punct and Digits <= dig and Minlen <= len(x)):

        y = hibp.hibp(x)
        if y==False:
            return False
        else:
            return True
    else:
        return False


# Generating password

#user name for pass_Gen function
def pass_Gen(user):
    u=user
    x = ''

    for i in range(15):

        """https://www.w3schools.com/python/ref_random_choices.asp"""
        x = x + (random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits))

    b=pass_Check(x)
    if b==True:
        p=x

        '''Python MySQL Insert Into Table W3 School'''
        "https://www.w3schools.com/python/python_mysql_insert.asp"
        Mycursor.execute('''Insert Into Access_table(id,Pass,Access,Date) Values(%s,%s,%s,%s)''', (u, p, 'user', DateOfMod,))
        mydb.commit()
        return p
    else:
        pass_Gen(u)





#Password in batch generation
def batch_Gen(b):
    with open(b, 'r') as csv_file:
        R = csv.reader(csv_file)
        next(R)


        for i in R:
            pass_Gen(i[1])


