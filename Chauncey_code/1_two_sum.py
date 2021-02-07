class Solution:
    def twoSum(self, nums, target: int):
        # Time: O(n)
        # Space: O(n)
        dict = {}

        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i


class Solution2:
    def twoSum(self, nums, target: int):
        # Two pointers, similar idea can work with 3sum
        # Time: O(nlogn)
        # Space: O(n)

        new_nums = [(num, idx) for idx, num in enumerate(nums)]
        sorted_nums = sorted(new_nums)
        i, j = 0, len(sorted_nums) - 1

        while i < j:
            if sorted_nums[i][0] + sorted_nums[j][0] == target:
                return sorted([sorted_nums[i][1], sorted_nums[j][1]])
            elif sorted_nums[i][0] + sorted_nums[j][0] > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':
    obj1 = Solution()
    obj2 = Solution2()
    nums = [2, 7, 11, 15]
    target = 9
    print(obj1.twoSum(nums, target))
    print(obj2.twoSum(nums, target))
