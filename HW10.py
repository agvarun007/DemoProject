# Leader of List:
def int_list(l1):
    l2 = []
    for i in l1:
        l2.append(int(i))
    return l2


list1 = input("Enter elements: ").split()
list2 = int_list(list1)
list1.clear()
fin_list = []

# Method 1: Brute Force
'''
for i in range(len(list2), 0, -1):
    list1.append(list2[i-1])
    if list2[i-1] == max(list1):
        fin_list.append(list2[i-1])
print("List of Leaders: ", fin_list)
'''

# Method 2: More efficient
'''
mx = list2[-1]
ctr = 0
for i in range(len(list2)-1, -1, -1):
    if mx < list2[i]:
        mx = list2[i]
        fin_list.append(mx)
        ctr += 1
if ctr == 0:
    fin_list.append(mx)
print("List of Leaders: ", fin_list)
'''