class Solution1:
    def removeKdigits(self, num: str, k: int) -> str:
        # Solution 1: select the min digits one by one for len(s) - k  times.
        # Time: O((n-k)*k)
        # Space: O(k)
        if k >= len(str(num)):
            return '0'

        s = str(num)
        res = ''
        position = -1

        for i in range(len(s) - k):
            search_start = max(i, position + 1)
            search_end = k + 1 + i
            digit, position = self.get_min_digit(s, search_start, search_end)
            res += digit

        return str(int(res))


    def get_min_digit(self, s, start, end):   # s is string of several integers.
        min_num = s[start]
        for digits in s[start: end]:
            if digits < min_num:
                min_num = digits

        min_position = s.find(min_num, start, end)

        return min_num, min_position


# ---------------------------------------------------------


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        # Solution 2: stack
        # Time: O(n)
        # Space: O(n)
        if k == 0:
            return str(num)
        if k >= len(str(num)):
            return '0'

        stack = []

        for digit in str(num):
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        res = int("".join(stack))
        return str(res)


if __name__ == '__main__':
    obj1 = Solution1()
    obj2 = Solution2()

    num1, k1 = '1432219', 3
    num2, k2 = '10200', 1
    num3, k3 = '10', 2

    print(obj1.removeKdigits(num1, k1))
    print(obj2.removeKdigits(num1, k1))

    print(obj1.removeKdigits(num2, k2))
    print(obj2.removeKdigits(num2, k2))

    print(obj1.removeKdigits(num3, k3))
    print(obj2.removeKdigits(num3, k3))
