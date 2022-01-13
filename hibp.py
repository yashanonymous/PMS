import requests
import hashlib

def hashing():
    buff="yash"
    y=hashlib.sha1(buff.encode('utf-8')).hexdigest()
    print(y)
    return y
y=hashing()
o=requests.get ("https://api.pwnedpasswords.com/range/"+y[:5])
#print(o.text)
for i in range(len(o.text)):
    print(o.text)
    '''if (y==o.text[j:k]):
        j=j+36
        k=k+39
        print("password leaked")
        break
    else:
        j=j+36
        k=k+39
        print("not leaked")'''
