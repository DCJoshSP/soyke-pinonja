#list recursion

def addNums(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + addNums(numlist[1:])
    #endif
#endfunc

marks = [3, 6, 2, 8, 1]
total = addNums(marks)
print(total)
