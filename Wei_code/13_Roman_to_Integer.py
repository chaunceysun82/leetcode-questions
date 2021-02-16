s = "MCMXCIV"

val_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

num = 0
last = 0

for i in range(len(s)):
    if val_map[s[i]] == last * 5 or val_map[s[i]] == last * 10:
        num = num + val_map[s[i]] - last
        last = 0
    else:
        num += last
        last = val_map[s[i]]

print(num + last)
