class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            if i == 0:
                cur = [1]
                
            elif i == 1:
                cur = [1,1]
                
            else:
                pre = res[i-1]
                cur = pre + [1]

                for j in range(1,len(cur)- 1):
                    cur[j] = pre[j-1]+pre[j]
                    
            res.append(cur)
                
        return res
