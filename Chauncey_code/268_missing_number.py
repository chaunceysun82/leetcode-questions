class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Time: O(N)
        # Space : O(1)

        n = len(nums)
        sum_index = 0
        sum_nums = 0

        for i, num in enumerate(nums):
            sum_index += i
            sum_nums += num

        return sum_index + n - sum_nums