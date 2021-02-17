class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)

        sum = 0
        res = []
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums