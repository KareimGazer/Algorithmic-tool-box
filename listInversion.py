def mergeAndCount(lst1, lst2, inv1, inv2):
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    index1, index2 = 0, 0
    result = list()
    invs = inv1 + inv2
    while(index1<lst1_len or index2<lst2_len):
        if(index1>=lst1_len):
            result.append(lst2[index2])
            index2 = index2 + 1
            invs = invs + lst1_len - index1
        elif(index2>=lst2_len):
            result.append(lst1[index1])
            index1 = index1 + 1  
        elif(lst1[index1]<lst2[index2]):
            result.append(lst1[index1])
            index1 = index1 + 1
        else:
            result.append(lst2[index2])
            index2 = index2 + 1
            invs = invs + lst1_len - index1
    
    return (result, invs)


def splitInversion(lst):
    if(len(lst)<2):
        return (lst, 0)
    else:
        halfLen = len(lst) // 2
        firstLst = lst[:halfLen]
        secondLst = lst[halfLen:]
        leftInversion, inv1 = splitInversion(firstLst)
        rightinversion, inv2 = splitInversion(secondLst)
        return mergeAndCount(leftInversion, rightinversion, inv1, inv2)


lst = [1,3,5,2,4,6]


print(splitInversion(lst)[1])

