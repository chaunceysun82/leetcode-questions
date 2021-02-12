class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        min_num = min(nums)
        moves = 0

        for num in nums:
            moves += num - min_num

        return moves