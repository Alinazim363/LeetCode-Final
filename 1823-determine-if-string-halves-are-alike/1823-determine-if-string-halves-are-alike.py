class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s)
        half = n // 2

        count_first = 0
        for i in range(half):
            if s[i] in vowels:
                count_first += 1

        count_second = 0
        for i in range(half, n):
            if s[i] in vowels:
                count_second += 1

        if count_first == count_second:
            return True
        else:
            return False      