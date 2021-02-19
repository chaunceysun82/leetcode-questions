class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0

        i = 1
        sum_left, sum_right = sum(nums[: i]), sum(nums[i + 1: ])

        while i < len(nums) - 1:
            if sum_left == sum_right:
                return i

            sum_left += nums[i]
            sum_right -= nums[i + 1]
            i += 1

        if sum(nums[:-1]) == 0:
            return len(nums) - 1

        return -1