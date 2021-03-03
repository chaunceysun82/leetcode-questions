DAIL_PANAL = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, [], results)

        return results

    def dfs(self, digits, index, combination, results):
        if index == len(digits):
            results.append(''.join(combination))
            return

        for ch in DAIL_PANAL[digits[index]]:
            combination.append(ch)
            self.dfs(digits, index + 1, combination, results)
            combination.pop()


obj = Solution()
digits = '23'
print(obj.letterCombinations(digits))
