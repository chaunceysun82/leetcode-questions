s = "loveleetcode"

import collections
count_dict = collections.Counter(s)

for i,ch in enumerate(s):
    if count_dict[ch] == 1:
        print(i)