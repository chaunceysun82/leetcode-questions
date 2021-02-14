class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        origin = x
        reversed = 0
        while x > 0:
            digit = x % 10
            x //= 10
            reversed = reversed * 10 + digit

        return origin == reversed


if __name__ == '__main__':
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))