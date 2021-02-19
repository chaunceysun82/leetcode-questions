class Solution:
    def climbStairs(self, n: int) -> int:
        # dp Time: O(n)
        # Space: O(n)
        if n == 1:
            return 1

        # dp[i] means how many distinct ways to reach step i. Result is dp[n]
        dp = [0] * (n + 1)

        # Initialization, dp[0] no actual meaning
        dp[1] = 1
        dp[2] = 2

        # Function
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp [i - 2]

        # Result
        return dp[n]