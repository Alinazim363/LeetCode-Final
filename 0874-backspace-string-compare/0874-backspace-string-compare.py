class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final_s = []
        for ch in s:
            if ch == '#':
                if final_s:
                    final_s.pop()
            else:
                final_s.append(ch)
    
        final_t = []
        for ch in t:
            if ch == '#':
                if final_t:
                    final_t.pop()
            else:
                final_t.append(ch)
                
        if final_s == final_t:
            return True
        else:
            return False