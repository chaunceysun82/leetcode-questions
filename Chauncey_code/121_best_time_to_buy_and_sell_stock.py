class Solution:
    def maxProfit(self, prices) -> int:
        # Sameway two pointer
        # Time: O(n)
        # Space: O(1)

        if len(prices) <= 1:
            return 0

        buy, sell = 0, 1
        max_profit = 0
        i = 0

        while i < len(prices):
            if prices[i] < prices[buy]:
                buy = i
                sell = min(buy + 1, len(prices) - 1)
            if prices[i] > prices[sell]:
                sell = i
            i += 1

            max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit


if __name__ == '__main__':
    obj = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(obj.maxProfit(prices))
