mylist = [1,2,3,4,5,6,6,6,6,6,7,8,9,10]

def binarysearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList) - 1
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if aList[midpoint] == itemSought:
            while aList[midpoint - 1] == itemSought:
                midpoint = midpoint - 1
            found = True
            index = midpoint
        else:
            if aList[midpoint] < itemSought:
                first = midpoint
            else:
                last = midpoint
    return index


print(binarysearch(mylist, 6))
