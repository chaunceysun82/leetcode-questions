nums =  [0]


i = j = 0
n = len(nums)

while j < n:
    if i == j and nums[i] != 0:
        i+=1
        j+=1
    elif nums[i] == 0:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        else:
            j += 1


print(nums)


