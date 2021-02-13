class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(n) n: all characters
        # Space: O(1)

        if not strs:    # need check this corner case
            return ''

        prefix = strs[0]
        for str in strs:
            prefix = self.get_prefix_for_two_str(prefix, str)

        return prefix

    def get_prefix_for_two_str(self, s1, s2):
        prefix = ''

        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                break
            prefix += s1[i]

        return prefix