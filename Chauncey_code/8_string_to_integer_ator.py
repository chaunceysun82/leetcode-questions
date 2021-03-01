class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        start = -1
        if not s:
            return 0

        if len(s) == 1 and not s[0].isdigit():
            return 0

        for i in range(len(s)):
            if start < 0 and not (s[i].isdigit() or s[i] in ['-', '+']):
                return 0

            if start < 0  and (s[i].isdigit() or s[i] in ['-', '+']):
                start = i
                continue

            if start >= 0 and not s[i].isdigit():
                end = i
                break
        else:
            end = len(s)

        s_num = s[start: end]

        if len(s_num) == 1 and not s_num[0].isdigit():
            return 0
        num = int(s_num)

        if num < -2 ** 31:
            return -2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 -1
        return num


obj = Solution()
s_list = [".1", "3.143", "   +-2342", "  -242", "", "4"]
for ch in s_list:
    print(obj.myAtoi(ch))