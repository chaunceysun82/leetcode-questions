class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p = len(numbers)//2

        list_len = len(numbers)
        
        while p >= 1 and numbers[p] > target:
            list_len = p
            p = p//2
            
            

        low, high = 0,list_len-1
        
        while numbers[low] + numbers[high] != target:
            sum = numbers[low] + numbers[high]
            if sum > target:
                high -= 1
            if sum < target:
                low += 1
                
        return [min(low+1, high+1),max(low+1, high+1)] 