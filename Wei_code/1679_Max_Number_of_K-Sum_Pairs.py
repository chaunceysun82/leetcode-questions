class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict_num = defaultdict(int)
        res = 0
        
        for num in nums:
            target = k - num
            if dict_num[target]:
                res += 1
                dict_num[target] -= 1
            else:
                dict_num[num] += 1
                
        return res