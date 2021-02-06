class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        # Time: O(n * k * 26) n: number of words, k: length of words
        # space: O(1)
        for i in range(len(words) - 1):
            if not self.is_sorted(words[i], words[i + 1], order):
                return False

        return True

    def is_sorted(self, s1, s2, order):
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                if order.find(s1[i]) > order.find(s2[i]):
                    return False
                return True
        else:
            if len(s1) > len(s2):
                return False

        return True


if __name__ == '__main__':
    obj = Solution()

    order = "hlabcdefgijkmnopqrstuvwxyz"
    words = ["hello","leetcode"]

    print(obj.isAlienSorted(words, order))