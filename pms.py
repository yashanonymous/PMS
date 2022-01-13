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


Mycursor=mydb.cursor()

print(date.today())

# policy file
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

def count(str1, str2):
    set_string1 = set(str1)
    set_string2 = set(str2)
    counted = set_string1 & set_string2
    return len(counted)




# Verifying password with policy
def passCheck(x):
    a = x

    up = count(a, string.ascii_uppercase)
    low = count(a, string.ascii_lowercase)
    punct = count(a, string.punctuation)
    dig = count(a, string.digits)

    if (Upper <= up and Lower <= low and Chars <= punct and Digits <= dig and Minlen <= len(x)):

        y=hibp.hashing(x)
        if y==0:
            passGen()
        else:
            print(y)
    else:

        passGen()


# Generating password
def passGen():
    x = ''
    for i in range(15):
        x = x + (random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits))

    passCheck(x)
    p=x
    return p

passGen()



#Password in batch generation
def batchGen():
    with open('users.csv', 'r') as csv_file:
        R = csv.reader(csv_file)
        next(R)
        #New File with Passwords
        with open('userspass.csv','w') as csv_file2:
            W = csv.writer(csv_file2,delimiter=' ')

            for i in R:
                p=passGen()
                W.writerow(i[0])
                W.writerow(i[1])
                W.writerow(p)
                '''Python MySQL Insert Into Table W3 School'''
                Mycursor.execute('''Insert Into Access_table(id,Username,Pass,Access,Date) Values(%s,%s,%s,%s,%s)''', (i[0],i[1],p,'User',DateOfMod,))


                mydb.commit()

batchGen()

with open('userspass.csv','r') as pswd_file:
    pwd=csv.reader(pswd_file,delimiter=' ')
    for i in pwd:
        print(i)