class Solution:
    def twoSum(self, nums, target: int):
        # Time: O(n)
        # Space: O(n)
        dict = {}

        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = obj.twoSum(nums, target)
    print(res)