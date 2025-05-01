class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string = ''.join(sorted(s))
        sorted_again = ''.join(sorted(t))

        if sorted_string == sorted_again:
            return True
        else:
            return False