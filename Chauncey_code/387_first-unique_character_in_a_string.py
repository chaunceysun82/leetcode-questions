from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = OrderedDict()

        for i, ch in enumerate(s):
            if ch in dict:
                count = dict.get(ch)[1] + 1
                dict[ch] = (i, count)
            else:
                dict[ch] = (i, 1)

        for value in dict.values():
            if value[1] == 1:
                return value[0]
        return -1


obj = Solution()
s = 'leetcode'
print(obj.firstUniqChar(s))