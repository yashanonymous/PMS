import requests
import hashlib

def hashing(buff):
    y=hashlib.sha1(buff.encode('utf-8')).hexdigest()
    print(y.upper())
    return y.upper()
o=requests.get ("https://api.pwnedpasswords.com/range/"+y[:5])
print(o.text)
print("-----------------------------------------------")
with open("hashes.txt",'w') as hash:
    hash.write(o.text)
with open("hashes.txt",'r') as hash:
    for i in hash:
        if (y[5:]==i[:35]):
            print('leaked')
            print(i)
            break
        else:
            print("not leaked")