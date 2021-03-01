class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(NlogN)
        # Space: O(N)
        return sorted([num ** 2 for num in nums])




class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)

        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n

        for k in range(n - 1, -1, -1):
            if abs(nums[i]) < abs(nums[j]):
                res[k] = nums[j] ** 2
                j -= 1
            else:
                res[k] = nums[i] ** 2
                i += 1

        return res
