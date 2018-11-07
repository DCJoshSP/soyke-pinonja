##Linear Search
numlist = [7,6,3,1,18,23,2,100]
alpha_list = ["A", "C", "D", "G", "M", "R", "W", "Z"]
def linearSearch(alist, item):
    index = -1
    i = 0
    found = False
    while i < len(alist) and found == False:
        if item == alist[i]:
            index = i
            found = True
        #endif
        i = i + 1
    #endwhile
    return index
#endfunction

print(linearSearch(numlist, 1))
print(linearSearch(numlist, 4))
print(linearSearch(alpha_list, "M"))
print(linearSearch(alpha_list, "N"))
        
