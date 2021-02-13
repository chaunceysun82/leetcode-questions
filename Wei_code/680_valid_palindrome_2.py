s = "aba"

for i in range(len(s)):
    if s[i] != s[-1-i]:
        break

n = len(s)
s1 = s[:i] + s[(i+1):]
s2 = s[:n-1-i] + s[n-i:]

print(s1)
print(s2)