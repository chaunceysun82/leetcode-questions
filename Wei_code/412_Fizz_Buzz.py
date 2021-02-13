class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nums = []
        for num in range(n):
            if (num + 1) % 15 == 0:
                nums.append("FizzBuzz")
            elif (num + 1) % 3 == 0:
                nums.append("Fizz")
            elif (num + 1) % 5 == 0:
                nums.append("Buzz")
            else:
                nums.append(str(num + 1))
                
        return nums
        