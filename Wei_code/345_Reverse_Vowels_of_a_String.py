class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        head = 0
        tail = len(s) - 1
        slist = []
        
        for ch in s:
            slist.append(ch)
            
        
        while head < tail:
            if slist[head] in vowel and slist[tail] in vowel:
                slist[head], slist[tail] = slist[tail], slist[head]
                head += 1
                tail -= 1
                
            elif slist[head] in vowel:
                tail -= 1
                
            elif slist[tail] in vowel:
                head += 1
                
            else:
                head += 1
                tail -= 1
                
        return ''.join(slist)