class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # Keep adding digits until it's a single digit
            num = sum(int(digit) for digit in str(num))
        return num

