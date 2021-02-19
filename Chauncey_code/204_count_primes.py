class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        arr = [0] * n
        arr[0] = 1
        arr[1] = 1

        sqrt = int(math.sqrt(n))
        for i in range(2, sqrt+1):
            j = 2
            while (i*j) < n:
                arr[i*j] = 1
                j += 1

        return len(arr) - sum(arr)