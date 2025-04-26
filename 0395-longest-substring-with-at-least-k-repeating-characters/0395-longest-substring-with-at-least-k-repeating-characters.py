class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
    
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
    
        for char, count in char_count.items():
            if count < k:
                substrings = s.split(char)
                return max(self.longestSubstring(substring, k) for substring in substrings)
    
        return len(s)    