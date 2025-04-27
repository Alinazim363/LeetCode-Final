class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

    # Traverse the digits from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set current digit to 0 if it's 9 (carryover)

    # If we finish the loop, it means all digits were 9, so add 1 at the front
        return [1] + digits