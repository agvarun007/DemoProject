# list1 = list(int(input()))
# print(list1)
# nested data type combination: List to dictionary

list2 = []
list3 = []
list1 = input("PLease give some values: ").split(' ')
for i in range(0, len(list1), 2):
    list2.append(list1[i])
    list3.append(list1[i+1])
list1 = zip(list2, list3)
dict1 = dict(list1)
print(dict1)