class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = ''

        while i >= 0 or j >= 0:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0

            nums_sum = num1 + num2 + carry
            digit = nums_sum % 2
            carry = nums_sum // 2
            res += str(digit)

            i -= 1
            j -= 1

        if carry > 0:
            res += str(carry)

        return res[::-1]