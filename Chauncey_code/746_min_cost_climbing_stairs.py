class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] means the min cost to reach ith step

        n = len(cost)
        dp = [0] * (n + 1)

        # initialization
        dp[0] = 0
        dp[1] = 0

        # equation

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # result
        return dp[n]