s = "A man, a plan, a canal: Panama"

filter_s = []
for ch in s:
    if ch.isalnum():
        filter_s += ch
        
ls = [ch.lower() for ch in filter_s]

print(ls == ls[::-1])