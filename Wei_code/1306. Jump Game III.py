class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def dfs(arr, i):
            if i < 0 or i >= len(arr):
                return False
            else:
                if arr[i] == 0:
                    return True
                elif i in ind_dict:
                    return False
                else:
                    ind_dict.add(i)
                
            return dfs(arr, i + arr[i]) or dfs(arr, i - arr[i])
            
        ind_dict = set()
        return dfs(arr,start)