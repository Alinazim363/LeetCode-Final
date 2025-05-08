class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ""               
        n = len(s)
    
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                ok = True
                for ch in set(sub):
                    if ch.islower():
                        if ch.upper() not in sub:
                            ok = False
                            break
                    else: 
                        if ch.lower() not in sub:
                            ok = False
                            break

                if ok and len(sub) > len(best):
                    best = sub
    
        return best        