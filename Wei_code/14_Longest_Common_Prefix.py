strs = ["flower","flow","flight"]

def prefix_two(str1,str2):
    n = min(len(str1), len(str2))
    prefix = str()
    
    for i in range(n):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break
    
    return prefix, i+1

prefix_min = prefix_two(strs[0],strs[1])
for i in range(1, len(strs)-1):
    prefix = prefix_two(strs[i],strs[i+1])
    if prefix[-1]<prefix_min[-1]:
        prefix_min = prefix

print(prefix_min[0])


