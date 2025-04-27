class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        if reverse == str(x):
            return True
        else:
            return False