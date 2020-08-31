import re


# IP Address:
def ipadd():
    ip = input("Enter IP address: ")
    res = re.findall(r'\d{3}.\d{1,3}.\d{1,3}.\d{1,3}', ip)
    print(res)


# Credit Card:
def ccd():
    cc = input("Enter CC No.: ")
    res = re.findall(r'[0-9]{16}', cc)
    print(res)


# Phone Number:
def phono():
    phno = input("Enter UAE Ph No: ")
    res = re.findall(r'\+9715[0-9]{8}', phno)
    print(res)


# E-Mail Address:
def emadd():
    str = input("Enter email id: ")
    res = re.findall(r'(^[a-z0-9]+)[_.a-z0-9]+\@[a-z]+(\.com)$', str)
    print(res)


ch = int(input(("""Choose option: 
                   1)IP Address
                   2)Credit Card
                   3)Phone No.
                   4)Email Address
                   ENTER (1-4): """)))
if ch == 1:
    ipadd()
elif ch == 2:
    ccd()
elif ch == 3:
    phono()
elif ch == 4:
    emadd()
else:
    print("Wrong Choice!")
    exit()
