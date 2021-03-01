class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        i, j = 0, n - 1
        s_list = list(s)

        while i <= j:
            while i <= j and s_list[i].lower() not in VOWELS:
                i += 1

            while i <= j  and s_list[j].lower() not in VOWELS:
                j -= 1

            if i <= j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

        return "".join(s_list)


obj = Solution()
print(obj.reverseVowels('hello'))