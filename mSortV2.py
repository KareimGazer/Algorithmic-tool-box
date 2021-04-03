def merge(lst1, lst2):
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    index1, index2 = 0, 0
    result = list()
    while(index1<lst1_len or index2<lst2_len):
        if(index1>=lst1_len):
            result.append(lst2[index2])
            index2 = index2 + 1
        elif(index2>=lst2_len):
            result.append(lst1[index1])
            index1 = index1 + 1  
        elif(lst1[index1]<lst2[index2]):
            result.append(lst1[index1])
            index1 = index1 + 1
        else:
            result.append(lst2[index2])
            index2 = index2 + 1
    
    return result


def mSort(lst):
    if(len(lst)<2):
        return lst
    else:
        halfLen = len(lst) // 2
        firstLst = lst[:halfLen]
        secondLst = lst[halfLen:]
        firstLst = mSort(firstLst)
        secondLst = mSort(secondLst)
        return merge(firstLst, secondLst)


lst = [4,6,5,2,3]


print(mSort(lst))
