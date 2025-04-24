class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0  # Base case: No valid substring possible
    
    # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
    
    # Find characters that occur less than k times
        for char, count in char_count.items():
            if count < k:
            # Split the string at 'char' and solve for each part
                substrings = s.split(char)
                return max(self.longestSubstring(substring, k) for substring in substrings)
    
    # If all characters have frequency >= k, the entire string is valid
        return len(s)    