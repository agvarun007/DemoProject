# Missing Number Problem:

def int_list(l1):
    l2 = []
    for i in l1:
        l2.append(int(i))
    return l2


list1 = input("Enter continuous elements with one element missing in the middle: ").split()
list2 = int_list(list1)
set1 = set(list2)
list2 = list(set1)
list2.sort()

# Method 1:
'''
osum = ((list2[-1] - list2[0] +1)*(list2[0] + list2[-1]))/2
isum = 0
for i in list2:
    isum += i
print("Missing element is: ", int(osum-isum))
'''

# Method 2:
'''
for i in range(len(list2)-1):
    if list2[i+1] - list2[i] == 2:
        missno = list2[i] + 1
        print("Missing element: ", int(missno))
'''