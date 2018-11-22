#Insertion sort

def insertionsort(alist):
    n = len(alist)
    for index in range(1, n):
        currentval = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > currentval:
            alist[pos] = alist[pos - 1]
            pos = pos - 1
        #endwhile
        alist[pos] = currentval
    #next index
    return alist
#endfunction

alist = [9,5,4,15,3,8,11]
print(insertionsort(alist))
