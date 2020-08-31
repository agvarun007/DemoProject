# Problem 1
# list1 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'xyz', 'xyz']
# list2 = list1
# for i in range(0, len(list2)):
#     count = 1
#     for j in range(i + 1, len(list2)):
#         if list2[i] == list2[j]:
#             count += 1
#             if count > 1:
#                 list2[j] = '0'
#
#     if count > 1 and list2[i] != '0':
#         print(list2[i], " is repeating ", count, " times ")

# Problem 2
# list1 = [('a', 'b'), ('c', 'd'), (1, 2), (4, 5)]
# dict1 = dict(list1)
# print(dict1)

# Problem 3
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [10, 20, 30, 40, 50]
# list3 = []
# for i in range(max(len(list1),len(list2))):
#     if i >= len(list1):
#         list3.append(list2[i])
#         continue
#     else:
#         list3.append(list1[i])
#     if i >= len(list2):
#         continue
#     else:
#         list3.append(list2[i])
# print(list3)

# Problem 4
# list1 = [1, 2, 3, 4, 4, 5, 6, 78, 11]
# list2 = [10, 1, 2, 50, 100]
# list3 = []
# com = 1
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             com = list1[i]*list2[j]
#         if com not in list3:
#             list3.append(com)
#             print("Square of common element: ", com)
