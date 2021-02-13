class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Time: O(n)

        if len(s) <= 2:
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                rest1, rest2 = s[i : j], s[i + 1: j + 1]
                return rest1 == rest1[::-1] or rest2 == rest2[::-1]

        return True