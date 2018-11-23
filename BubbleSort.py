def bubblesort(nums):
    j = 0
    i = 0
    swapped = True
    while i < (len(nums) - 1) and swapped == True:
        swapped = False
        for i in range(0,len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            #endif
        #next
        j = j + 1
    #next
    return nums
#endfunction
nums = [7,5,2,7,8,9,4,1]
print(bubblesort(nums))
