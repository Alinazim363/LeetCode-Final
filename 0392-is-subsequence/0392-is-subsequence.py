class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1

        return i == len(s)        