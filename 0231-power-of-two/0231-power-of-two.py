class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:  # Keep dividing by 2
            n //= 2
        return n == 1