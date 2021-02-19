class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        sum_list = []
        sum_list.append(nums[0])
        
        for i in range(1, len(nums)):
            sum_list.append(sum_list[i-1] + nums[i])
            
        return sum_list