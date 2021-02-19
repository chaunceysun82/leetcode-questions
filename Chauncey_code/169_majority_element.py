from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        return Counter(nums).most_common(1)[0][0]