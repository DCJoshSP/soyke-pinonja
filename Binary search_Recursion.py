mylist = [1,2,3,4,5,6,6,6,6,6,7,8,9,10]


def binsearch(aList, item, first, last):
    if last < first:
        return -1
    else:
        midpoint = (first + last) // 2
        if aList[midpoint] > item:
            return binsearch(aList, item, first, midpoint - 1)
        else:
            if aList[midpoint] < item:
                return binsearch(aList, item, midpoint + 1, last)
            else:
                while aList[midpoint - 1] == item:
                    midpoint = midpoint - 1
                return midpoint
            #endif
        #endif
    #endif
#endfunc

print(binsearch(mylist, 6, 0 ,13))
