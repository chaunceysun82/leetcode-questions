class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Time: O(NlogN)
        # Space O(logN)

        nums.sort()
        count = 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1

            elif nums[i] + nums[j] > k:
                j -= 1

            else:
                i += 1

        return count
