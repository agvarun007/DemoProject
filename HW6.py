randstr = 'this is string to play$@! if $#$you can###'
list1 = randstr.split(" ")
randlist = []
list2 = []
for i in range(0, len(list1)):
    randlist = list(list1[i])
    j = 0
    k = len(randlist) - 1
    while j < k:
        if not randlist[j].isalpha():
            j += 1
        elif not randlist[k].isalpha():
            k -= 1
        else:
            randlist[j], randlist[k] = randlist[k], randlist[j]
            j += 1
            k -= 1
    randstr = ''.join(randlist)
    list2.append(randstr)
randstr = " ".join(list2)
print(randstr)
