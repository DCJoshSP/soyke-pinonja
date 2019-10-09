##Linear Search
numlist = [7,6,4,18,18,9,4,11]
alpha_list = ["A", "M", "D", "G", "M", "R", "W", "N"]
def linearSearch(alist, item):
    index = []
    i = 0
    while i < len(alist):
        if item == alist[i]:
            index.append(i)
        #endif
        i = i + 1
    #endwhile
    return index
#endfunction



print(linearSearch(numlist, 18))
print(linearSearch(numlist, 4))
print(linearSearch(alpha_list, "M"))
print(linearSearch(alpha_list, "N"))
        
