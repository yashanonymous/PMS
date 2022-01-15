import requests
import hashlib
"""https://docs.python.org/3/library/hashlib.html"""
def hibp(buff):
    y=hashlib.sha1(buff.encode('utf-8')).hexdigest()
    y=y.upper()
    x=check(y)
    if x == 0:
        return False
    else:
        return True
def check(y):
    """https://www.w3schools.com/python/module_requests.asp"""

    o=requests.get ("https://api.pwnedpasswords.com/range/"+y[:5])

    with open("hashes.txt",'w') as hash:
        hash.write(o.text)
    x=1
    with open("hashes.txt",'r') as hash:
        for i in hash:
            if (y[5:]==i[:35]):
                x=0
                break

    return x

