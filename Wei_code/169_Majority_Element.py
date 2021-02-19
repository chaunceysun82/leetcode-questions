import collections
nums = [2,2,1,1,1,2,2]

count = collections.Counter(nums)

result = nums[0]

if len(nums) == 0:
    print(result)

for i in range(1,len(nums)):
    if count[nums[i]] > count[result]:
        result = nums[i]

print(result)
