class Solution:
    def countAndSay(self, n: int) -> str:
        # Time: O

        if n == 1:
            return '1'

        output = '1'
        for _ in range(n - 1):
            output = self.get_next(output)

        return output

    def get_next(self, s):
        i, j = 0, 0
        count = 0
        res = ''

        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            count = j - i
            res += (str(count) + s[i])
            i = j

        return res