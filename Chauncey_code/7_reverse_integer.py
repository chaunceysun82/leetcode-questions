class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > 2**31 - 1:
            return 0
        s = str(abs(x))[::-1]
        if abs(int(s)) > 2**31 -1:
            return 0
        return int(s) if x > 0 else -int(s)
