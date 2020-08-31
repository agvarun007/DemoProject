# Problem 1:
# [1,1,1,2,2,3,3,3,3,5,5,5,5,5,7,7,7,7,7]
# write function
# input to this will be list
# a=3
# [7, 5, 3]
# a=2
# [7,5]

"""
def int_list(l1):
    l2 = []
    for i in l1:
        l2.append(int(i))
    return l2


def finalist(n, l1, sl):
    no_list = []
    for j in range(n):
        mx = max(l1)
        ind = l1.index(mx)
        no_list.append(sl[ind])
        sl.remove(sl[ind])
        l1.remove(mx)
    return no_list


list1 = input("enter elements for the list: ").split()
list2 = int_list(list1)
list1.clear()
set1 = set(list2)
set_list = list(set1)
for i in set_list:
    x = list2.count(i)
    list1.append(x)

no = int(input("Enter the no. of top elements that you wish to print: "))
if no > len(set_list):
    print("You have entered a number bigger than the no. of different elements")
    exit()
print(finalist(no, list1, set_list))
"""

# Problem 2:
# string1 = 'thethe'
# string1 = " this is the test of Varun and Haniya"
# we have to find the first character that is repeated
from typing import Dict

"""
s1 = input("Enter string: ")
sc = s1[::]
list1 = []
list2 = []
for i in range(len(sc)):
    for j in range(i+1, len(s1)):
        if sc[i] == s1[j]:
            list1.append(sc[i])
            list2.append(j)
            continue
mn = min(list2)
ind = list2.index(mn)
print(list1[ind])
"""