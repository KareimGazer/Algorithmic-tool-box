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
    if(len(lst)==2):
        #print("==2")
        if(lst[0]<=lst[1]):
            #print(lst)
            return lst
        else:
            result = [lst[1], lst[0]]
            #print(result)
            return result
    elif(len(lst)<2):
        #print('<2')
        #print(lst)
        return lst
    else:
        #print("else")
        halfLen = len(lst) // 2
        firstLst = lst[:halfLen]
        secondLst = lst[halfLen:]
        #print(firstLst)
        #print(secondLst)
        firstLst = mSort(firstLst)
        #print(firstLst)
        secondLst = mSort(secondLst)
        #print(secondLst)
        #print(firstLst)
        return merge(firstLst, secondLst)


lst = [4,6,5,2,3]


print(mSort(lst))