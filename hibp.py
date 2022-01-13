import requests
import hashlib

def hashing(buff):
    y=hashlib.sha1(buff.encode('utf-8')).hexdigest()
    print(y.upper())
    y=y.upper()
    x=hibp(y)
    if x == 0:
        return x
    else:
        return buff
def hibp(y):
    o=requests.get ("https://api.pwnedpasswords.com/range/"+y[:5])
    print(o.text)
    print("-----------------------------------------------")
    with open("hashes.txt",'w') as hash:
        hash.write(o.text)
    x=1
    with open("hashes.txt",'r') as hash:
        for i in hash:
            if (y[5:]==i[:35]):
                print('leaked')
                x=0
                print(i)
                break
            else:
                print("not leaked")
    return x
