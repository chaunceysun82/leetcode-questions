class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ''

        while i >= 0 or j >= 0:
            number1 = ord(num1[i]) - ord('0') if i >= 0 else 0  # ord() works
            number2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            nums_sum = number1 + number2 + carry
            carry = nums_sum // 10
            digit = nums_sum % 10
            res += str(digit)

            i -= 1
            j -= 1

        if carry > 0:
            res += str(carry)

        return res[::-1]


if __name__ == '__main__':
    obj = Solution()
    num1 = '23423'
    num2 = '982332'
    print(obj.addStrings(num1, num2))