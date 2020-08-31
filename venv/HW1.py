randstr = "this is the string"
list1 = randstr.split(" ")
for i in range(0,len(list1)):
    list1[i] = list1[i][::-1]
randstr = " ".join(list1)
print(randstr)
