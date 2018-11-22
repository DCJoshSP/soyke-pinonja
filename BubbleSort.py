def bubblesort(nums):
    x = True
    if x == True:
        x = False
        for j in range(0,len(nums)):
            for i in range(0,len(nums) - 1 - j):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    x = True
                #endif
            #next
        #next
    #endif
    return nums
#endfunction
nums = [1,6,4,3,8,7,9,2]
print(bubblesort(nums))
