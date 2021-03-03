        i = j = 0
        sub_nums = []
        
        while nums[i] < 0 and i < len(nums)-1:
            sub_nums.append(nums[i]**2)
            i += 1
            
        while len(sub_nums) != 0 and i < len(nums):
            if nums[i]**2 <= sub_nums[-1]:
                nums[j] = nums[i]**2
                i += 1
                j += 1
            else:
                nums[j] = sub_nums[-1]
                j += 1
                sub_nums.pop()
                
        if len(sub_nums) == 0:
            for i in range(i, len(nums)):
                nums[i] = nums[i]**2
                
        else:
            while len(sub_nums) != 0:
                nums[j] = sub_nums[-1]
                j += 1
                sub_nums.pop()
                
        return nums
