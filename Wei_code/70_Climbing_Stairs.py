"""class Solution:
    def climbStairs(self, n: int, memo = None) -> int:
        if n == 0: 
            return 1
        if n == 1:
            return 1
        
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        result = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        
        memo[n] = result
        
        return result"""


n = 6
if n <= 3: print(n)

n_2 = 1
n_1 = 2
curr = 3

while curr < n:
    new_n = n_2 + n_1
    n_2 = n_1
    n_1 = new_n
    curr += 1

print(n_2 + n_1)