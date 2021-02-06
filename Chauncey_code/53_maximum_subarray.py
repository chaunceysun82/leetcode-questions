class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)

        # state - dp[i] the largest sum of subarry ending with index i
        dp = [0] * n

        # Initialization
        dp[0] = nums[0]

        # function
        for i in range(n - 1):
            dp[i + 1] = max(0, dp[i]) + nums[i + 1]

        # answer - max in dp
        return max(dp)