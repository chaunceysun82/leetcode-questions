class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b

        return a