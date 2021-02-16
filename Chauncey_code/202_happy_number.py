class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []

        while (n not in nums):
            nums.append(n)
            n = self.get_next_num(n)
            if n == 1:
                return True
        return False

    def get_next_num(self, n):
        new_num = 0
        while n > 0:
            digit = n % 10
            n //= 10
            new_num += digit ** 2

        return new_num


obj = Solution()
print(obj.isHappy(19))
